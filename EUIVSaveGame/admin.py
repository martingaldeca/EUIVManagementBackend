from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import EuIVSaveGame, EuIVPathConfig


@admin.register(EuIVSaveGame)
class SaveGameAdmin(SimpleHistoryAdmin):
    list_display = (
        'id',
        'savegame_name',
        'savegame_date',
        'savegame_file',
        'savegame_size',
        'host_user',
        'active',
    )
    readonly_fields = ('savegame_date', 'creation_datetime', 'modification_datetime', 'savegame_lines', 'savegame_size', 'savegame_dlc_enabled',)
    search_fields = ('savegame_name', 'savegame_date')
    actions = ('process_savegame', 'record_session')

    def process_savegame(self, request, queryset):
        for savegame in queryset:
            savegame.process_file()

    def record_session(self, request, queryset):
        for savegame in queryset:
            savegame.record_session()


@admin.register(EuIVPathConfig)
class EuIVPathConfigAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'creation_datetime',
        'modification_datetime',
        'euiv_path',
    )
    list_filter = ('creation_datetime', 'modification_datetime')
    actions = ('get_file_games_in_path',)

    def get_file_games_in_path(self, request, queryset):
        for path in queryset:
            path.get_all_savegames_in_path()
