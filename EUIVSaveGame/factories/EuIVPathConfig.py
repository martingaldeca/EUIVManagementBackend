from EUIVSaveGame.models import EuIVPathConfig
from factory.django import DjangoModelFactory


class EuIVPathConfigFactory(DjangoModelFactory):
    class Meta:
        model = EuIVPathConfig
        django_get_or_create = ('euiv_path',)

    euiv_path = './'
