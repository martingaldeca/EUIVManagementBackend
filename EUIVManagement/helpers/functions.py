import os
from datetime import datetime


def transform_eu4_date(euiv_date: str = None) -> datetime:
    """
    Function to return the datetime from the euiv date format
    :param euiv_date:
    :return:
    """
    if euiv_date is None:
        return None
    return datetime.strptime(euiv_date, '%Y.%m.%d')


def get_file_size(file_name: str) -> float:
    """
    Function to get the size of the file
    :param file_name:
    :return:
    """
    size_in_bytes = os.path.getsize(file_name)
    return size_in_bytes / (1024 * 1024)


def get_list_of_files(dir_name: str) -> list:
    """
    Create a list of file and sub directories
    names in the given directory

    :param dir_name:
    :return:
    """
    list_of_file = os.listdir(dir_name)
    all_files = list()

    # Iterate over all the entries
    for entry in list_of_file:

        # Create full path
        full_path = os.path.join(dir_name, entry)

        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + get_list_of_files(full_path)
        else:
            all_files.append(full_path)

    return all_files


def clean_database_for_tests():
    from EUIVSaveGame.models import EuIVPathConfig, EuIVSaveGame
    from EUIVCountries.models import EuIVCountry, EuIVProvince
    from EUIVUserManagement.models import EuIVUser, EuIVUserProfile, EuIVUserActiveGames
    from EUIVStats.models import EuIVCountryStats, EuIVProvinceStats
    EuIVSaveGame.objects.all().delete()
    EuIVPathConfig.objects.all().delete()
    EuIVCountry.objects.all().delete()
    EuIVProvince.objects.all().delete()
    EuIVUser.objects.all().delete()
    EuIVUserProfile.objects.all().delete()
    EuIVUserActiveGames.objects.all().delete()
    EuIVCountryStats.objects.all().delete()
    EuIVProvinceStats.objects.all().delete()
