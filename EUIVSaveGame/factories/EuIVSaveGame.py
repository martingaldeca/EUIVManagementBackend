import datetime

from factory.fuzzy import FuzzyDate

from EUIVSaveGame.models import EuIVSaveGame
from EUIVSaveGame.factories import EuIVPathConfigFactory
from factory.django import DjangoModelFactory
import factory


class EuIVSaveGameFactory(DjangoModelFactory):
    class Meta:
        model = EuIVSaveGame
        django_get_or_create = ('savegame_file',)

    euiv_path = factory.SubFactory(EuIVPathConfigFactory)
    savegame_file = factory.django.FileField(filename='fake_file.eu4')
    savegame_lines = 1000
    savegame_size = 1000
    savegame_name = 'Fake savegame'
    savegame_description = 'Fake description'
    savegame_date = FuzzyDate(datetime.date(1994, 8, 8))
    savegame_dlc_enabled = [
        'Conquest of Paradise', 'Art of War', 'El Dorado', 'Common Sense', 'The Cossacks', 'Mare Nostrum', 'Rights of Man', 'Mandate of Heaven', 'Third Rome',
        'Cradle of Civilization', 'Dharma', 'Golden Century'
    ]
    savegame_is_multi_player = True
    savegame_checksum = '123'
    active = True
    check_time = 1600
