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

    def get_queryset(self):
        final_query = self.model.objects.all()
        return final_query
