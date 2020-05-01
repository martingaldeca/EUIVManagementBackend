from operator import itemgetter

from django.db.models import Max
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from logging import getLogger

from EUIVStats.models import EuIVCountryStats
from EUIVCountries.models import EuIVCountry
from EUIVUserManagement.models import EuIVUserActiveGames, EuIVUser

logger = getLogger(__name__)


class BestSavegamePlayersByStatView(APIView):

    def get(self, request: Request, savegame_name: int, stat: str):
        # Get all the countries that the users control in the game. Could be many, for example Castile and Spain
        user_active_games = EuIVUserActiveGames.objects.filter(save_game__savegame_name=savegame_name).values('country', 'user')
        country_ids = [user_active_game.get('country') for user_active_game in user_active_games]

        # Get the stats of all the countries but the last date
        max_date = EuIVCountryStats.objects.filter(save_game__savegame_name=savegame_name).aggregate(Max('stats_date'))
        country_stats = EuIVCountryStats.objects.filter(save_game__savegame_name=savegame_name, country__id__in=country_ids, stats_date=max_date['stats_date__max']).values(stat, 'country')

        total_data = []
        for user_active_game in user_active_games:
            user = EuIVUser.objects.get(id=user_active_game['user'])
            country = EuIVCountry.objects.get(id=user_active_game['country'])
            total_data.append([
                f'{user.username} [{country.name}]',
                country.get_color(),
                [country_stat[stat] if country_stat[stat] is not None else 0 for country_stat in country_stats if country_stat['country'] == country.id][0]
            ])

        # Order the data from top to bottom stat
        total_data_ordered = sorted(total_data, key=itemgetter(2), reverse=True)

        # Append 0 value for represent in the graphic
        total_data_ordered.append(['', '', 0])

        player_names = []
        background_colors = []
        stat_data = []
        for total_single_data in total_data_ordered:
            player_names.append(total_single_data[0])
            background_colors.append(total_single_data[1])
            stat_data.append(total_single_data[2])

        best_players_in_game_by_stat = {
            'hoverBackgroundColor': "red",
            'hoverBorderWidth': 10,
            'labels': player_names,
            'datasets': [
                {
                    'label': f'{stat.replace("_", " ").capitalize()}',
                    'backgroundColor': background_colors,
                    'data': stat_data,
                }
            ],
        }

        return Response(best_players_in_game_by_stat, status.HTTP_200_OK)
