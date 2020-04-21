from rest_framework.response import Response
from rest_framework.views import APIView
import os
from operator import itemgetter
from django.db.models import Max
from logging import getLogger
from EUIVSaveGame.models import EuIVSaveGame
from EUIVStats.models import EuIVCountryStats
from EUIVUserManagement.models import EuIVUser, EuIVUserActiveGames
from rest_framework.status import HTTP_200_OK

logger = getLogger(__name__)


class EuIVPlatformInfo(APIView):

    @staticmethod
    def get(request):
        """
        Get the platform principal info
        :param request:
        :return:
        """
        database_size = round(os.path.getsize('euiv') / (1024 * 1024), 2)
        if database_size <= 1000:
            units = 'MB'
        else:
            database_size = database_size / 1024
            units = 'GB'
        total_savegames = EuIVSaveGame.objects.all().count()
        total_multiplayer = EuIVSaveGame.objects.filter(savegame_is_multi_player=True).count()
        total_users = EuIVUser.objects.all().count()

        # Get the chart info
        multiplayer_vs_singleplayer = [total_savegames - total_multiplayer, total_multiplayer]

        # Get the best players info from the stats
        # Get all the user games and the max development value for the countries the played in their savegames
        development_list = []
        for user_active_game in EuIVUserActiveGames.objects.all():
            country = user_active_game.country
            save_game = user_active_game.save_game
            user = user_active_game.user
            max_development = EuIVCountryStats.objects.filter(save_game=save_game, country=country).aggregate(Max('development'))

            # Sometimes there is no data in the savegame for this user (if he was only in the lobby)
            if type(max_development['development__max']) is not float:
                continue
            development_list.append([f'{user.username}[{country.name}]', country.get_color(), max_development['development__max']])

        # Now order the values by the development and get the first 10 positions
        development_list_ordered = sorted(development_list, key=itemgetter(2), reverse=True)[:10]

        # Create the lists to render in the frontend
        best_players_names = []
        best_players_colors = []
        best_players_development = []
        for development_list_ordered_value in development_list_ordered:
            best_players_names.append(development_list_ordered_value[0])
            best_players_colors.append(development_list_ordered_value[1])
            best_players_development.append(development_list_ordered_value[2])

        # Create the dict with the information of the best players
        best_players_data = {
            'best_players_names': best_players_names,
            'best_players_colors': best_players_colors,
            'best_players_development': best_players_development
        }

        response = {
            'size': database_size,
            'units': units,
            'total_savegames': total_savegames,
            'total_multiplayer': total_multiplayer,
            'total_users': total_users,
            'multiplayer_vs_singleplayer': multiplayer_vs_singleplayer,
            'best_players_data': best_players_data
        }
        return Response(response, status=HTTP_200_OK)
