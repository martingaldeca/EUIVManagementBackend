from django.urls import path

from EUIVSaveGame.rest.views import (
    EuIVSaveGameList, EuIVSimpleSaveGameList, ProcessSavegamesInPath,
    ChangeCheckTimeView, GetCheckTimeView, ChangeHitsUntilEndOfStreamingView, GetHitsUntilEndOfRecordView,
    RecordSessionView
)

urlpatterns = [
    path('save_games/', EuIVSaveGameList.as_view(), name='list_save_games'),
    path('simple_save_games/<int:user_id>/', EuIVSimpleSaveGameList.as_view(), name='list_save_games'),
    path('process_path/', ProcessSavegamesInPath.as_view(), name='process_path'),
    path('change_check_time/', ChangeCheckTimeView.as_view(), name='change_check_time'),
    path('get_check_time/<str:savegame_name>/', GetCheckTimeView.as_view(), name='get_check_time'),
    path('change_hits_until_end_of_streaming/', ChangeHitsUntilEndOfStreamingView.as_view(), name='change_hits_until_end_of_streaming'),
    path('get_hits_until_end_of_streaming/<str:savegame_name>/', GetHitsUntilEndOfRecordView.as_view(), name='get_hits_until_end_of_streaming'),
    path('record_session/', RecordSessionView.as_view(), name='record_session'),
]
