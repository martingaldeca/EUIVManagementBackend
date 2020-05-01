from django.urls import path

from EUIVStats.rest.views import EuIVProvinceStatsList, UserCountryStatView, BestSavegamePlayersByStatView

urlpatterns = [
    path('province_stats/', EuIVProvinceStatsList.as_view(), name='list_province_stats'),
    path('country_stat/<str:stat>/<str:savegame_name>/<int:user_id>/', UserCountryStatView.as_view(), name='user_country_stat'),
    path('best_savegame_players/<str:stat>/<str:savegame_name>/', BestSavegamePlayersByStatView.as_view(), name='best_savegame_players'),
]
