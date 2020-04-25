from logging import getLogger

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from EUIVSaveGame.models import EuIVPathConfig

logger = getLogger(__name__)


class ProcessSavegamesInPath(APIView):

    @staticmethod
    def post(request: Request):
        """
        With this get we receive as parameter the path to process, we create or get the path in the model and process all savegames info.
        :param request:
        :return:
        """

        # Get the path and check if it was passed in the request, if it is not we return a 404
        path = request.data.get('path', None)
        if path is None or path == '':
            return Response('The path was not set.', status.HTTP_400_BAD_REQUEST)

        # Create the dict info that the frontend will manage
        response_data = ''

        # Get the path in the model, if it has been created we will sent to the frontend the info
        path_to_explore, create = EuIVPathConfig.objects.get_or_create(euiv_path=path)
        if create:
            logger.info(f'Will add a new savegames path "{path}" to the database.')
            response_data += 'Path added to the database, '

        # Now get all the savegames and process them process the savegame
        try:
            total_not_editable_savegames, total_editable_savegames = path_to_explore.get_and_process_all_savegames_in_path(force_reprocess=True)
        except FileNotFoundError:

            # If the path can not be found in the computer we will delete the path and send to the frontend the info with a 404
            path_to_explore.delete()
            return Response(f'Can not find {path} in the system.', status.HTTP_404_NOT_FOUND)
        except PermissionError:
            path_to_explore.delete()
            return Response(f'Denied access to {path}.', status.HTTP_401_UNAUTHORIZED)

        response_data += f'Path successfully  processed, {total_not_editable_savegames} savegames can be read and {total_editable_savegames} can not.'

        return Response(response_data, status.HTTP_200_OK)
