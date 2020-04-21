from django.urls import path

from EUIVSaveGame.rest.views import EuIVSaveGameList, EuIVSimpleSaveGameList

urlpatterns = [
    path('save_games/', EuIVSaveGameList.as_view(), name='list_save_games'),
    path('simple_save_games/', EuIVSimpleSaveGameList.as_view(), name='list_save_games'),
]
