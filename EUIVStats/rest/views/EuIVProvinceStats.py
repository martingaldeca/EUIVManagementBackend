from EUIVManagement.helpers import EuIVListCreateAPIView
from EUIVStats.rest.serializers import EuIVProvinceStatsSerializer
from EUIVStats.models import EuIVProvinceStats


class EuIVProvinceStatsList(EuIVListCreateAPIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.serializer_class = EuIVProvinceStatsSerializer
        self.model = EuIVProvinceStats

        self.ordering_fields = [field.name for field in self.model._meta.fields]
        self.filterset_fields = [field.name for field in self.model._meta.fields]
