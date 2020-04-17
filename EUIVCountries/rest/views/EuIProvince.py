from EUIVManagement.helpers import EuIVListCreateAPIView
from EUIVCountries.rest.serializers import EuIVProvinceSerializer
from EUIVCountries.models import EuIVProvince


class EuIVProvinceList(EuIVListCreateAPIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.serializer_class = EuIVProvinceSerializer
        self.model = EuIVProvince

        self.ordering_fields = [field.name for field in self.model._meta.fields]
        self.filterset_fields = [field.name for field in self.model._meta.fields]
