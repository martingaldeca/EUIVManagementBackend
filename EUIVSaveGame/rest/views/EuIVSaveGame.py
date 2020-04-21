from EUIVManagement.helpers import EuIVListCreateAPIView
from EUIVSaveGame.rest.serializers import EuIVSaveGameSerializer, EuIVSimpleSaveGameSerializer
from EUIVSaveGame.models import EuIVSaveGame


class EuIVSaveGameList(EuIVListCreateAPIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.serializer_class = EuIVSaveGameSerializer
        self.model = EuIVSaveGame

        self.ordering_fields = [field.name for field in self.model._meta.fields]
        self.filterset_fields = [field.name for field in self.model._meta.fields]


class EuIVSimpleSaveGameList(EuIVListCreateAPIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.serializer_class = EuIVSimpleSaveGameSerializer
        self.model = EuIVSaveGame

        self.ordering_fields = [field.name for field in self.model._meta.fields]
        self.filterset_fields = [field.name for field in self.model._meta.fields]
