from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from EUIVManagement.helpers import EuIVListCreateAPIView
from EUIVSaveGame.rest.serializers import EuIVSaveGameSerializer, EuIVSimpleSaveGameSerializer
from EUIVSaveGame.models import EuIVSaveGame
from EUIVUserManagement.models import EuIVUser, EuIVUserActiveGames

from logging import getLogger

logger = getLogger(__name__)


class EuIVSaveGameList(EuIVListCreateAPIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.serializer_class = EuIVSaveGameSerializer
        self.model = EuIVSaveGame

        self.ordering_fields = [field.name for field in self.model._meta.fields]
        self.filterset_fields = [field.name for field in self.model._meta.fields]


class EuIVSimpleSaveGameList(APIView):

    def get(self, request: Request, user_id: int = None):
        """
        Return all the savegames where the user is playing.

        If it is a superuser it will return all the savegames
        :param request:
        :param user_id:
        :return:
        """
        user = EuIVUser.objects.get(id=user_id)
        if user.is_superuser:
            serializer = EuIVSimpleSaveGameSerializer(EuIVSaveGame.objects.all(), many=True).data
            return Response(serializer, status.HTTP_200_OK)

        # Get all the savegames of the user
        user_games = EuIVUserActiveGames.objects.filter(user=user).values('save_game')
        serializer = EuIVSimpleSaveGameSerializer(EuIVSaveGame.objects.filter(id__in=[user_game['save_game'] for user_game in user_games]), many=True).data
        return Response(serializer, status.HTTP_200_OK)


class ChangeCheckTimeView(APIView):

    @staticmethod
    def post(request: Request):
        """
        Post to change the check time of a savegame
        :param request:
        :return:
        """
        savegame_name = request.data.get('savegame_name', None)
        check_time = request.data.get('check_time', None)
        if check_time is None or check_time == '':
            return Response('Check time was not set.', status.HTTP_400_BAD_REQUEST)
        try:
            check_time = float(check_time)
        except ValueError:
            return Response('Check time must be a number.', status.HTTP_400_BAD_REQUEST)

        if savegame_name is None:
            return Response('Internal error, please report the issue.', status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Check that the value is correct
        if check_time < 1:
            return Response(f'The min value for check time param is 1, {check_time} is not valid.', status.HTTP_400_BAD_REQUEST)

        try:
            savegame = EuIVSaveGame.objects.get(savegame_name=savegame_name)
        except EuIVSaveGame.DoesNotExist:
            return Response(f'Internal error, please report the issue. Savegame does not exists.', status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Transform to minutes
        check_time *= 60

        # Change the check time
        logger.debug(f'Check time for "{savegame}" will change from "{savegame.check_time}" to "{check_time}".')
        savegame.check_time = check_time
        savegame.save()

        return Response(f'Check time was set to {check_time} seconds.', status.HTTP_200_OK)


class GetCheckTimeView(APIView):

    def get(self, request: Request, savegame_name: str):
        try:
            savegame = EuIVSaveGame.objects.get(savegame_name=savegame_name)
        except EuIVSaveGame.DoesNotExist:
            return Response(f'Internal error, please report the issue. Savegame does not exists.', status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(savegame.check_time / 60, status.HTTP_200_OK)


class ChangeHitsUntilEndOfStreamingView(APIView):

    @staticmethod
    def post(request: Request):
        """
        Post to change the check time of a savegame
        :param request:
        :return:
        """
        savegame_name = request.data.get('savegame_name', None)
        hits_until_end_of_streaming = request.data.get('hits_until_end_of_streaming', None)
        if hits_until_end_of_streaming is None or hits_until_end_of_streaming == '':
            return Response('Check time was not set.', status.HTTP_400_BAD_REQUEST)
        try:
            hits_until_end_of_streaming = int(hits_until_end_of_streaming)
        except ValueError:
            return Response('Check time must be a integer.', status.HTTP_400_BAD_REQUEST)

        if savegame_name is None:
            return Response('Internal error, please report the issue.', status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Check that the value is correct
        if hits_until_end_of_streaming < 1 or hits_until_end_of_streaming > 10:
            return Response(f'The value must be between 1 and 10, {hits_until_end_of_streaming} is not valid.', status.HTTP_400_BAD_REQUEST)

        try:
            savegame = EuIVSaveGame.objects.get(savegame_name=savegame_name)
        except EuIVSaveGame.DoesNotExist:
            return Response(f'Internal error, please report the issue. Savegame does not exists.', status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Change the hits_until_end_of_streaming
        logger.debug(f'Hits until end of record for "{savegame}" will change from "{savegame.hits_until_end_of_streaming}" to "{hits_until_end_of_streaming}".')
        savegame.hits_until_end_of_streaming = hits_until_end_of_streaming
        savegame.save()

        return Response(f'Hits until end of record was set to {hits_until_end_of_streaming}.', status.HTTP_200_OK)


class GetHitsUntilEndOfRecordView(APIView):

    def get(self, request: Request, savegame_name: str):
        try:
            savegame = EuIVSaveGame.objects.get(savegame_name=savegame_name)
        except EuIVSaveGame.DoesNotExist:
            return Response(f'Internal error, please report the issue. Savegame does not exists.', status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(savegame.hits_until_end_of_streaming, status.HTTP_200_OK)
