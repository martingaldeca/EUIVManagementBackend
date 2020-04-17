from django.db import models
from EUIVManagement.helpers import EuIVModel
from EUIVSaveGame.models import EuIVSaveGame
from EUIVCountries.models import EuIVCountry


class EuIVCountryStats(EuIVModel):
    # Basic info of the stat
    save_game = models.ForeignKey(EuIVSaveGame, null=True, blank=True, verbose_name='Save game', help_text='Save game associated to the country info.', on_delete=models.CASCADE, db_index=True)
    stats_date = models.DateField(auto_now=False, blank=True, null=True, verbose_name='Stats date', help_text='Current date in the savegame when the screenshot.', db_index=True)
    country = models.ForeignKey(EuIVCountry, null=True, blank=True, verbose_name='Country', help_text='Current country for the info.', on_delete=models.CASCADE, db_index=True)

    # Custom info for the country
    current_power_projection = models.FloatField(blank=True, null=True, verbose_name='Power projection', help_text='Current power projection of the country.')
    great_power_score = models.FloatField(blank=True, null=True, verbose_name='Great power score', help_text='Current great power score of the country.')
    development = models.FloatField(blank=True, null=True, verbose_name='Development', help_text='Current development of the country.')
    raw_development = models.FloatField(blank=True, null=True, verbose_name='Raw development', help_text='Current raw development of the country.')
    capped_development = models.FloatField(blank=True, null=True, verbose_name='Capped development', help_text='Current capped development of the country.')
    realm_development = models.FloatField(blank=True, null=True, verbose_name='Realm development', help_text='Current realm development of the country.')
    base_tax = models.FloatField(blank=True, null=True, verbose_name='Base tax', help_text='Current base tax of the country.')
    adm_tech = models.IntegerField(blank=True, null=True, verbose_name='Administrative technology', help_text='Current administrative technology of the country.')
    dip_tech = models.IntegerField(blank=True, null=True, verbose_name='Diplomatic technology', help_text='Current diplomatic technology of the country.')
    mil_tech = models.IntegerField(blank=True, null=True, verbose_name='Military technology', help_text='Current military technology of the country.')
    navy_strength = models.FloatField(blank=True, null=True, verbose_name='Navy strength', help_text='Current navy strength of the country.')
    num_owned_home_cores = models.IntegerField(blank=True, null=True, verbose_name='Total owned home cores', help_text='Current total owned home cores of the country.')
    num_of_controlled_cities = models.IntegerField(blank=True, null=True, verbose_name='Total controlled cities', help_text='Current total controlled cities of the country.')
    num_of_total_ports = models.IntegerField(blank=True, null=True, verbose_name='Total ports', help_text='Current total ports of the country.')
    forts = models.IntegerField(blank=True, null=True, verbose_name='Forts', help_text='Current forts of the country.')
    average_effective_unrest = models.FloatField(blank=True, null=True, verbose_name='Average unrest', help_text='Current average unrest of the country.')
    average_autonomy = models.FloatField(blank=True, null=True, verbose_name='Average autonomy', help_text='Current autonomy of the country.')
    num_of_allies = models.IntegerField(blank=True, null=True, verbose_name='Total allies', help_text='Current total allies of the country.')
    prestige = models.FloatField(blank=True, null=True, verbose_name='Prestige', help_text='Current prestige of the country.')
    stability = models.FloatField(blank=True, null=True, verbose_name='Stability', help_text='Current stability of the country.')
    treasury = models.FloatField(blank=True, null=True, verbose_name='Treasury', help_text='Current treasury of the country.')
    inflation = models.FloatField(blank=True, null=True, verbose_name='Inflation', help_text='Current inflation of the country.')
    total_owned_provinces = models.IntegerField(blank=True, null=True, verbose_name='Total owned provinces', help_text='Current total owned provinces of the country.')
    total_controlled_provinces = models.IntegerField(blank=True, null=True, verbose_name='Total controlled provinces', help_text='Current total controlled provinces of the country.')
    army_tradition = models.FloatField(blank=True, null=True, verbose_name='Army tradition', help_text='Current army tradition of the country.')
    navy_tradition = models.FloatField(blank=True, null=True, verbose_name='Navy tradition', help_text='Current navy tradition of the country.')
    last_month_income = models.FloatField(blank=True, null=True, verbose_name='Last month income', help_text='Current last month income of the country.')
    last_month_expense = models.FloatField(blank=True, null=True, verbose_name='Last month expense', help_text='Current last month expense of the country.')
    estimated_loan = models.FloatField(blank=True, null=True, verbose_name='Estimated loan', help_text='Current estimated loan of the country.')
    corruption = models.FloatField(blank=True, null=True, verbose_name='Corruption', help_text='Current corruption of the country.')
    legitimacy = models.FloatField(blank=True, null=True, verbose_name='Legitimacy', help_text='Current legitimacy of the country.')
    mercantilism = models.FloatField(blank=True, null=True, verbose_name='Mercantilism', help_text='Current mercantilism of the country.')
    splendor = models.FloatField(blank=True, null=True, verbose_name='Splendor', help_text='Current splendor of the country.')
    army_professionalism = models.FloatField(blank=True, null=True, verbose_name='Army professionalism', help_text='Current army professionalism of the country.')
    government = models.CharField(null=True, blank=True, verbose_name='Government', help_text='Current government of the country.', max_length=50)
    manpower = models.FloatField(blank=True, null=True, verbose_name='Manpower', help_text='Current manpower of the country.')
    max_manpower = models.FloatField(blank=True, null=True, verbose_name='Max manpower', help_text='Current max manpower of the country.')
    sailors = models.FloatField(blank=True, null=True, verbose_name='Sailors', help_text='Current sailors of the country.')
    max_sailors = models.FloatField(blank=True, null=True, verbose_name='Max sailors', help_text='Current max sailors of the country.')
    is_great_power = models.BooleanField(blank=False, null=False, default=False, verbose_name='Great power', help_text='Indicate if the country is great power.', db_index=True)
    government_reform_progress = models.FloatField(blank=True, null=True, verbose_name='Government reform progress', help_text='Current max sailors of the country.')

    class Meta:
        verbose_name = 'Country stat'

    def __str__(self):
        return f'Stats for {self.save_game} - {self.country} - {self.stats_date}'
