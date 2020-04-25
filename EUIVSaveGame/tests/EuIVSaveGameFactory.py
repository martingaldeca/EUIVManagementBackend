import datetime

from django.test import TestCase
from EUIVSaveGame.factories import EuIVPathConfigFactory
from EUIVSaveGame.models import EuIVSaveGame
from EUIVSaveGame.parser import parse_save_game_lines
from EUIVManagement.helpers.functions import transform_eu4_date

from EUIVManagement.helpers import clean_database_for_tests


class EuIVSaveGameTestCase(TestCase):

    def setUp(self) -> None:
        self.path_config_string = './EUIVSaveGame/tests/'
        self.path_config = EuIVPathConfigFactory(euiv_path=self.path_config_string)

    def tearDown(self) -> None:
        clean_database_for_tests()

    def test_savegame_creation(self):
        self.path_config.get_and_process_all_savegames_in_path()
        save_game = EuIVSaveGame.objects.get(euiv_path=self.path_config)
        self.assertEqual('test_lines_multiplayer', save_game.savegame_name)
        with open(save_game.savegame_file) as eu_file:
            file_lines = eu_file.readlines()
        eu_file.close()
        raw_dict = parse_save_game_lines(file_lines)
        self.assertEqual('1994.8.8', raw_dict['date'])
        self.assertEqual('"Kittens"', raw_dict['displayed_country_name'])
        self.assertEqual(datetime.datetime(1994, 8, 8, 0, 0), transform_eu4_date(raw_dict['date']))
