from django.db import models, IntegrityError
from EUIVSaveGame.models import EuIVSaveGame
from logging import getLogger
from EUIVManagement.helpers import get_list_of_files, get_file_size, EuIVModel

from EUIVManagement.helpers import timeit

logger = getLogger(__name__)


class EuIVPathConfig(EuIVModel):
    euiv_path = models.CharField(null=False, unique=True, blank=True, db_index=True, verbose_name='EUIV savegame path', help_text='Savegame path in your computer.', max_length=500)

    class Meta:
        verbose_name = 'Path config'

    def __str__(self):
        return self.euiv_path

    @timeit
    def get_and_process_all_savegames_in_path(self, force_reprocess: bool = False) -> list:
        """
        Function to explore the path and look for all savegames files
        :param: force_reprocess
        :return:
        """
        logger.info(f"Getting all savegames in path {self}.")

        # Go recursively to all files in path
        save_games = get_list_of_files(self.euiv_path)
        logger.info(f"Files in path are = {save_games}")

        # Create the variables to collect the number of savegames that can be edited and that can not be edited
        total_not_editable_savegames = 0
        total_editable_savegames = 0

        # Save all files as saved files if extension is .eu4
        save_games = [save_game for save_game in save_games if '.eu4' in save_game]
        logger.info(f'All the savegames are {save_games}')
        for save_game in save_games:

            # Open the file if is not Iron Man
            try:
                with open(save_game) as eu_file:
                    file_lines = eu_file.readlines()

                    save_game_object, created = EuIVSaveGame.objects.get_or_create(
                        euiv_path=self,
                        savegame_file=eu_file.name,
                    )
                    if not created:
                        logger.info(f"The savegame {save_game_object} existed in the database.")
                        if force_reprocess:
                            save_game_object.process_file()
                    else:
                        save_game_object.savegame_lines = len(file_lines)
                        save_game_object.savegame_size = get_file_size(save_game)
                        save_game_object.save()
                        save_game_object.process_file()
                eu_file.close()
                total_editable_savegames += 1

            except UnicodeDecodeError:
                logger.info(f"The file '{save_game}'  is an IronMan savegame, EUIVManagement can not extract info from it.")
                total_not_editable_savegames += 1

            except IntegrityError:
                logger.info(f"The savegame '{save_game}' was previously associated to other path, it will be skip.")
                total_editable_savegames += 1
                if force_reprocess:
                    save_game_object = EuIVSaveGame.objects.get(savegame_file=eu_file.name)
                    save_game_object.process_file()
        return [total_not_editable_savegames, total_editable_savegames]
