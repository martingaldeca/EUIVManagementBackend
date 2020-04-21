from EUIVManagement.helpers import EuIVListCreateAPIView
from EUIVCountries.rest.serializers import EuIVCountrySerializer
from EUIVCountries.models import EuIVCountry


class EuIVCountryList(EuIVListCreateAPIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.serializer_class = EuIVCountrySerializer
        self.model = EuIVCountry

        self.ordering_fields = [field.name for field in self.model._meta.fields]
        self.filterset_fields = [field.name for field in self.model._meta.fields]
