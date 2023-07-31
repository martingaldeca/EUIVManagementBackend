import threading
import time
import uuid
from typing import List

from django.db import models, IntegrityError
from django.core.validators import MaxValueValidator, MinValueValidator
from EUIVManagement.helpers import EuIVModel, get_file_size, transform_eu4_date, timeit
from logging import getLogger
from EUIVSaveGame.parser import parse_save_game_lines
from EUIVCountries.models import EuIVCountry, EuIVProvince

logger = getLogger(__name__)


class EuIVSaveGame(EuIVModel):
    # Path with savegames associated
    euiv_path = models.ForeignKey('EuIVPathConfig', null=False, blank=False, verbose_name='Savegames path.', help_text='The path where the savegame is stored.', on_delete=models.CASCADE)

    # Fields associate with the file itself
    savegame_file = models.CharField(null=False, unique=True, blank=True, db_index=True, verbose_name='EUIV savegame file', help_text='Savegame file in your computer.', max_length=500)
    savegame_lines = models.IntegerField(verbose_name='Savegame lines', help_text='Number of total lines in the savegame.', default=-1, blank=False, null=False)
    savegame_size = models.FloatField(verbose_name='Savegame size (MB)', help_text='Size in MB of the savegame.', default=-1, blank=False, null=False)

    # Complementary fields provided by the user
    savegame_name = models.CharField(
        max_length=50, default=uuid.uuid4(), verbose_name='Savegame name', help_text='The name of the savegame to use.', blank=False, null=False, db_index=True, unique=True
    )
    savegame_description = models.CharField(max_length=300, verbose_name='Savegame description', help_text='The description of the savegame.', blank=True, null=True)

    # Info obtained from the file
    savegame_date = models.DateField(auto_now=False, blank=True, null=True, verbose_name='Savegame date', help_text='Current date in the savegame.', db_index=True)
    savegame_dlc_enabled = models.CharField(max_length=1000, blank=True, null=True, verbose_name='DLC enabled', help_text='List of dlcs enabled in the savegame.')

    savegame_is_multi_player = models.BooleanField(blank=True, null=True, verbose_name='Multiplayer', help_text='Boolean that indicate if the savegame is a multi player game.', db_index=True)
    host_user = models.ForeignKey('EUIVUserManagement.EuIVUser', blank=True, null=True, db_index=True, verbose_name='Host user', help_text='The host of the savegame.', on_delete=models.CASCADE)
    savegame_checksum = models.CharField(max_length=100, blank=True, null=True, verbose_name='Savegame Checksum', help_text='Checksum of the savegame.')

    # Fields for schedule the auto process of the save game
    active = models.BooleanField(blank=False, null=False, default=False, verbose_name='Active', help_text='Field that indicates if the savegame is been playing right now.', db_index=True)
    check_time = models.FloatField(
        blank=False, null=False, default=60 * 10, verbose_name='Check time', help_text='The time to wait until the next check in seconds (from 5 minutes to 1 hour)',
        validators=[MinValueValidator(60 * 5), MaxValueValidator(60 * 60)]
    )
    hits_until_end_of_streaming = models.IntegerField(
        blank=False, null=False, default=3, verbose_name='Record max hits',
        help_text='The number of savegame process without changes until the end of stream.', validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    class Meta:
        verbose_name = 'Save game'

    def __str__(self):
        return f'{self.savegame_name}'

    @timeit
    def process_file(self):
        """
        Function to process savegame file.

        The process can be of an active game or hard process of a file.

        If the savegame is active instead of look to the auto save game, and will associate the stats to that.
        :return:
        """

        savegame_file_to_read = self.savegame_file
        if self.active:
            logger.info(f"Will process the autosave file for the active game {self}")
            autosave_name = 'mp_autosave' if self.savegame_is_multi_player else 'autosave'
            autosave, created = EuIVSaveGame.objects.get_or_create(savegame_name=autosave_name)
            if created:
                logger.info(f"There is not any autosave yet in the path {self.euiv_path}. File {self.savegame_file} it is going to be processed.")
                savegame_file_to_read = self.savegame_file
            else:
                savegame_file_to_read = autosave.savegame_file
        else:
            logger.info(f"Will process raw info of '{self}'.")
        with open(savegame_file_to_read) as eu_file:
            file_lines = eu_file.readlines()
        eu_file.close()

        # Update the internal values
        self.savegame_lines = len(file_lines)
        self.savegame_size = get_file_size(self.savegame_file)

        # Parse the file lines in a cached dict
        # We will only process the info if the savegame has change
        if file_lines[-1].split('=')[1] != self.savegame_checksum:
            raw_dict = parse_save_game_lines(file_lines)
            rebel_dict = self.get_sub_dict(raw_dict, 'rebel_faction')

            # Get the checksum
            self.savegame_checksum = raw_dict.get('checksum', None)

            # Get the save name
            self.savegame_name = self.savegame_file.split('\\')[-1].replace('mp_autosave ', '').replace('.eu4', '').replace('"', '')

            # Get the savegame date
            self.savegame_date = transform_eu4_date(raw_dict.get('date', None))

            # Get the enabled dlcs
            self.savegame_dlc_enabled = raw_dict.get('dlc_enabled', None)

            # Get if is a multiplayer game
            self.savegame_is_multi_player = raw_dict.get('multi_player', None) == 'yes'

            # If is multiplayer get the payers info
            if self.savegame_is_multi_player:
                self.get_multi_players_info(raw_dict.get('players_countries', None), raw_dict.get('player', '').replace('"', ''))

            # Get the provinces stats
            province_dict = raw_dict['provinces']
            del raw_dict['provinces']
            self.save_province_stats(province_dict)

            # Get the countries stats
            countries_dict = raw_dict['countries']
            del raw_dict['countries']
            self.save_countries_stats(countries_dict)

            self.save()

        else:
            logger.info('The savegame file to process was previously processed.')

    @timeit
    def save_countries_stats(self, countries_dict: dict = None) -> None:
        from EUIVStats.models import EuIVCountryStats

        all_countries_stats = []
        date = self.savegame_date

        # Check if there is any stat for the savegame in the concrete date (we will only save 1 point per date
        if EuIVCountryStats.objects.filter(save_game=self, stats_date=date).count() != 0:
            return

        # Read all the countries info
        for country_identifier, country_info in countries_dict.items():

            # Get the country color
            country_color = country_info.get('colors', {'country_color': '0, 0, 0'}).get('country_color', None)

            # Get the country
            try:
                country, created = EuIVCountry.objects.get_or_create(tag=country_identifier, color=country_color)
            except IntegrityError:
                country, created = EuIVCountry.objects.get_or_create(tag=country_identifier)
                logger.info(f"The country '{country_identifier}' will update it's color from '{country.color}' to '{country_color}'.")
                country.color = country_color
                country.save()

            # Get the army and navy sub dicts
            army_dict = self.get_sub_dict(country_info, key_to_look='army', excluded_keys=['army_professionalism', 'max_historic_army_professionalism', 'army_tradition', 'army_templates'])
            navy_dict = self.get_sub_dict(country_info, key_to_look='navy', excluded_keys=['navy_strength', 'navy_tradition', 'navy_templates'])

            # Get concrete stats
            country_stats_dict = {
                'save_game': self,
                'stats_date': date,
                'country': country,
                'current_power_projection': country_info.get(
                    'current_power_projection', None
                ),
                'great_power_score': country_info.get('great_power_score', None),
                'development': country_info.get('development', None),
                'raw_development': country_info.get('raw_development', None),
                'capped_development': country_info.get('capped_development', None),
                'realm_development': country_info.get('realm_development', None),
                'base_tax': country_info.get('base_tax', None),
                'adm_tech': country_info.get('technology', {'adm_tech': None}).get(
                    'adm_tech', None
                ),
                'dip_tech': country_info.get('technology', {'dip_tech': None}).get(
                    'dip_tech', None
                ),
                'mil_tech': country_info.get('technology', {'mil_tech': None}).get(
                    'mil_tech', None
                ),
                'navy_strength': country_info.get('navy_strength', None),
                'num_owned_home_cores': country_info.get(
                    'num_owned_home_cores', None
                ),
                'num_of_controlled_cities': country_info.get(
                    'num_of_controlled_cities', None
                ),
                'num_of_total_ports': country_info.get('num_of_total_ports', None),
                'forts': country_info.get('forts', None),
                'average_effective_unrest': country_info.get(
                    'average_effective_unrest', None
                ),
                'average_autonomy': country_info.get('average_autonomy', None),
                'num_of_allies': country_info.get('num_of_allies', None),
                'prestige': country_info.get('prestige', None),
                'stability': country_info.get('stability', None),
                'treasury': country_info.get('treasury', None),
                'inflation': country_info.get('inflation', None),
                'total_owned_provinces': len(
                    country_info.get('owned_provinces', [])
                ),
                'total_controlled_provinces': len(
                    country_info.get('controlled_provinces', [])
                ),
                'army_tradition': country_info.get('army_tradition', None),
                'navy_tradition': country_info.get('navy_tradition', None),
                'last_month_income': country_info.get(
                    'ledger', {'lastmonthincome': None}
                ).get('lastmonthincome', None),
                'last_month_expense': country_info.get(
                    'ledger', {'lastmonthexpense': None}
                ).get('lastmonthexpense', None),
                'estimated_loan': country_info.get('estimated_loan', None),
                'corruption': country_info.get('corruption', None),
                'legitimacy': country_info.get('legitimacy', None),
                'mercantilism': country_info.get('mercantilism', None),
                'splendor': country_info.get('splendor', None),
                'army_professionalism': country_info.get(
                    'army_professionalism', None
                ),
                'government': country_info.get(
                    'government', {'government': 'No government'}
                )
                .get('government', 'No government')
                .replace('"', ''),
                'manpower': country_info.get('manpower', None),
                'max_manpower': country_info.get('max_manpower', None),
                'sailors': country_info.get('sailors', None),
                'max_sailors': country_info.get('max_sailors', None),
                'is_great_power': country_info.get('is_great_power', 'no')
                == 'yes',
                'government_reform_progress': country_info.get(
                    'government_reform_progress', None
                ),
            }
            all_countries_stats.append(
                EuIVCountryStats(**country_stats_dict)
            )

        # Save all the data
        EuIVCountryStats.objects.bulk_create(all_countries_stats)
        logger.info(f'{len(all_countries_stats)} country stats saved for {self} at {date}.')

    @timeit
    def save_province_stats(self, province_dict: dict = None) -> None:
        """
        Function to save the province stats of the savegame.
        :param province_dict:
        :return:
        """
        from EUIVStats.models import EuIVProvinceStats

        # A lot of information, so we will save it in bulk
        all_province_stats = []

        # Check if there is any stat for the savegame in the concrete date (we will only save 1 point per date
        date = self.savegame_date
        if EuIVProvinceStats.objects.filter(save_game=self, stats_date=date).count() != 0:
            return

        # Read all the province info
        for province_identifier, province_info in province_dict.items():
            # Get main province-date info

            province_name = province_info.get('name', 'NO_NAME').replace('"', '')
            try:
                province, created = EuIVProvince.objects.get_or_create(identifier=province_identifier, name=province_name)
            except IntegrityError:
                province, created = EuIVProvince.objects.get_or_create(identifier=province_identifier)
                logger.info(f"The province '{province_identifier}' will update it's name from '{province.name}' to '{province_name}'.")
                province.name = province_name
                province.save()

            # Get concrete stats
            development = province_info.get('original_tax', None)
            base_tax = province_info.get('base_tax', None)
            base_production = province_info.get('base_production', None)
            base_manpower = province_info.get('base_manpower', None)
            trade_power = province_info.get('trade_power', None)
            owner, created = EuIVCountry.objects.get_or_create(tag=province_info.get('owner', 'NO_ONE').replace('"', ''))
            controller, created = EuIVCountry.objects.get_or_create(tag=province_info.get('controller', 'NO_ONE').replace('"', ''))
            devastation = province_info.get('devastation', None)

            all_province_stats.append(
                EuIVProvinceStats(
                    save_game=self,
                    stats_date=date,
                    province=province,
                    development=development,
                    base_tax=base_tax,
                    base_production=base_production,
                    base_manpower=base_manpower,
                    trade_power=trade_power,
                    owner=owner,
                    controller=controller,
                    devastation=devastation
                )
            )

        # Save all the data
        EuIVProvinceStats.objects.bulk_create(all_province_stats)
        logger.info(f'{len(all_province_stats)} province stats saved for {self} at {date}.')

    def get_multi_players_info(self, players_countries: List[str] = None, host_country: str = None):
        """
        With this function parse the players info and save it in the model
        :param host_country:
        :param players_countries:
        :return:
        """
        # Must import here the EuIVUser in order to avoid circular dependencies
        from EUIVUserManagement.models import EuIVUser, EuIVUserActiveGames

        # The list is in a player, country way, so we must nested
        players_list = [players_countries[i:i + 2] for i in range(0, len(players_countries), 2)]

        for player in players_list:
            user, created = EuIVUser.objects.get_or_create(username=player[0])
            country, created = EuIVCountry.objects.get_or_create(tag=player[1])

            # Only save the savegame if it was not saved
            EuIVUserActiveGames.objects.get_or_create(user=user, save_game=self, country=country)

            # Check if the player is the host
            if player[1] == host_country:
                self.host_user = user

    @staticmethod
    def get_sub_dict(raw_dict: dict = None, key_to_look: str = '', force_exact: bool = False, excluded_keys: list = ()) -> dict:
        """
        Function to obtain a sub dict from one dict.

        It also will del all the keys of the sub dict values in the raw dict to avoid have information repeated
        :param excluded_keys:
        :param force_exact:
        :param key_to_look:
        :param raw_dict:
        :return:
        """
        sub_dict = {}
        keys_to_del = []
        for key, value in raw_dict.items():
            if ((force_exact and key_to_look == key) or (not force_exact and key_to_look in key)) and key not in excluded_keys:
                key_name = f'{key_to_look}_{value["id"]["id"]}'
                sub_dict[key_name] = value
                keys_to_del.append(key)

        for key in keys_to_del:
            if key in raw_dict:
                del raw_dict[key]

        return sub_dict

    def control_in_save(self, force_save: bool = False, **kwargs):
        """
        Check if there is any other active savegame. If it is the case we will close the previous active savegame and set this as active.

        :param force_save: Parameter to force the update if needeed
        :return:
        """

        # Check if the savegame is active and if the force save is not set
        if self.active and not force_save:

            # Get all the active savegames excluding current and check if there is any
            active_savegames = EuIVSaveGame.objects.filter(active=True).exclude(id=self.id)
            if active_savegames.count() > 0:
                logger.info(f'There are {active_savegames.count} active savegames. All of them will be closed for set {self} as active.')
                for active_savegame in active_savegames:
                    active_savegame.active = False
                    active_savegame.save(force_save=True)

    def record_session(self):
        """
        With this function we start to process the file in a thread
        :return:
        """
        logger.info(f"The savegame {self} will be recorded.")
        self.active = True
        self.save()
        threading.Thread(target=process_file_while_active, args=(self,)).start()


def process_file_while_active(save_game: EuIVSaveGame):
    """
    Function to thread for get statistics in game
    :param save_game:
    :return:
    """
    logger.info(f"Will record {save_game} stats.")
    # Will only run if the game is active
    counter = 0
    while save_game.active:
        # Get the previous checksum of the file
        previous_checksum = save_game.savegame_checksum

        # Get the object info in each interaction
        save_game = EuIVSaveGame.objects.get(id=save_game.id)
        save_game.process_file()

        # If the checksum has not change means that is the same file, and we should stop record
        if save_game.savegame_checksum == previous_checksum:
            counter += 1
            logger.info(f"The session game for {save_game} seems to be ended.")
            if counter == save_game.hits_until_end_of_streaming:
                save_game.active = False
                save_game.save()
        else:
            counter = 0

        # Wait until next execution
        time.sleep(save_game.check_time)
    logger.info(f"The session game {save_game} ended.")
