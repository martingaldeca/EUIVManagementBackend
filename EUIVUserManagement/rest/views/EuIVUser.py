from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from EUIVManagement.helpers import EuIVListCreateAPIView
from EUIVUserManagement.rest.serializers import EuIVUserProfileSerializer, EuIVSimpleUserProfileSerializer
from EUIVUserManagement.models import EuIVUserProfile, EuIVUser
from logging import getLogger

logger = getLogger(__name__)


class EuIVUserProfileList(EuIVListCreateAPIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.serializer_class = EuIVUserProfileSerializer
        self.model = EuIVUserProfile

        self.ordering_fields = [field.name for field in self.model._meta.fields if field.name != 'user_avatar']
        self.filterset_fields = [field.name for field in self.model._meta.fields if field.name != 'user_avatar']

        self.extra_filters = ['user__username', ]


class EuIVSimpleUsersList(EuIVListCreateAPIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.serializer_class = EuIVSimpleUserProfileSerializer
        self.model = EuIVUserProfile

        self.ordering_fields = None
        self.filterset_fields = None


class ResetEuUserPassword(APIView):

    def put(self, request, pk, format=None):

        # Get the new password the old password and if is the first login
        new_password = request.data.get('newPassword', None)
        old_password = request.data.get('oldPassword', None)
        first_login = request.data.get('firstLogin', False)
        if new_password is None or old_password is None:
            return Response('Password was not send', status=status.HTTP_400_BAD_REQUEST)

        # Get the user from the primary key, it should be created if not something wrong ins happening. Probably an attack
        user, created = EuIVUser.objects.get_or_create(pk=pk)
        if created:
            msg = 'User was not in the platform, ¿How did you enter here?. This incident will be reported and investigated.'
            logger.warning(msg)
            return Response(msg, status=status.HTTP_418_IM_A_TEAPOT)

        if not user.check_password(old_password):
            return Response('The password was incorrect', status=status.HTTP_401_UNAUTHORIZED)
        user.set_password(new_password)
        user.save()

        user_profile_to_serialize = EuIVUserProfile.objects.get(user=user)

        if first_login:
            user_profile_to_serialize.first_login = False
            user_profile_to_serialize.save()
        serializer = EuIVUserProfileSerializer(user_profile_to_serialize).data
        return Response(serializer, status=status.HTTP_200_OK)
