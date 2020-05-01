from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from logging import getLogger

from EUIVStats.models import EuIVCountryStats
from EUIVCountries.models import EuIVCountry
from EUIVUserManagement.models import EuIVUserActiveGames

logger = getLogger(__name__)


class UserCountryStatView(APIView):

    def get(self, request: Request, savegame_name: int, user_id: int, stat: str):
        # Get all the countries that the user controlled in the game. Could be many, for example Castile and Spain
        countries = EuIVUserActiveGames.objects.filter(user=user_id, save_game__savegame_name=savegame_name).values('country')
        country_ids = [country.get('country') for country in countries]
        countries_info = EuIVCountry.objects.filter(id__in=country_ids)

        # Get the stats of all the countries
        country_stats = EuIVCountryStats.objects.filter(save_game__savegame_name=savegame_name, country__id__in=country_ids).values('stats_date', stat, 'country')
        datasets = []
        for country_id in country_ids:
            country_info = countries_info.get(id=country_id)
            dataset = {
                'label': f'{country_info.name} {stat.replace("_", " ").capitalize()}',
                'data': [{'x': country_stat['stats_date'], 'y': country_stat[stat]} for country_stat in country_stats if country_stat['country'] == country_id],
                'fill': False,
                'borderColor': country_info.get_color()
            }
            datasets.append(dataset)

        country_stat_info = {'datasets': datasets}

        return Response(country_stat_info, status.HTTP_200_OK)
