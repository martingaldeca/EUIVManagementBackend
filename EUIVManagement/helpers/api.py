from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from EUIVManagement.helpers import EuIVModel


class EuIVListCreateAPIView(ListCreateAPIView):
    authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.filter_backends = [DjangoFilterBackend]
        self.model = EuIVModel

        self.extra_filters = []

    def get_queryset(self):
        final_query = self.model.objects.all()

        # Check if there is any extra filter in the queryset and if the model has any extra filter
        # if it is the case, just simply filter by this field
        if len(self.extra_filters) > 0 and len(self.request.query_params) > 0:
            extra_filter_dict = {}
            for extra_filter in self.extra_filters:
                extra_filter_dict[extra_filter] = self.request.query_params.get(extra_filter)
            final_query = final_query.filter(**extra_filter_dict)

        return final_query
