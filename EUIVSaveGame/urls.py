from django.urls import path

from EUIVSaveGame.rest.views import EuIVSaveGameList, EuIVSimpleSaveGameList, ProcessSavegamesInPath

urlpatterns = [
    path('save_games/', EuIVSaveGameList.as_view(), name='list_save_games'),
    path('simple_save_games/', EuIVSimpleSaveGameList.as_view(), name='list_save_games'),
    path('process_path/', ProcessSavegamesInPath.as_view(), name='process_path'),
]
