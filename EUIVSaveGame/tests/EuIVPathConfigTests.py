from django.test import TestCase
from EUIVSaveGame.factories import EuIVPathConfigFactory

from EUIVManagement.helpers import clean_database_for_tests


class EuIVPathConfigTestCase(TestCase):

    def setUp(self) -> None:
        self.path_config_string = './EUIVSaveGame/tests/'
        self.path_config = EuIVPathConfigFactory(euiv_path=self.path_config_string)

    def tearDown(self) -> None:
        clean_database_for_tests()

    def test_path_creation(self):
        self.assertEqual(self.path_config_string, self.path_config.euiv_path)
        [total_not_editable_savegames, total_editable_savegames] = self.path_config.get_and_process_all_savegames_in_path()
        self.assertEqual([0, 1], [total_not_editable_savegames, total_editable_savegames])

    def test_no_permissions_path(self):
        no_permissions_path = EuIVPathConfigFactory(euiv_path='/')
        with self.assertRaises(PermissionError):
            no_permissions_path.get_and_process_all_savegames_in_path()

    def test_no_path_set(self):
        with self.assertRaises(ValueError):
            EuIVPathConfigFactory(euiv_path=None)

    def test_file_not_found(self):
        no_path_set = EuIVPathConfigFactory(euiv_path='')
        with self.assertRaises(FileNotFoundError):
            no_path_set.get_and_process_all_savegames_in_path()
        no_path_set = EuIVPathConfigFactory(euiv_path='I_am_a_fake_path')
        with self.assertRaises(FileNotFoundError):
            no_path_set.get_and_process_all_savegames_in_path()

