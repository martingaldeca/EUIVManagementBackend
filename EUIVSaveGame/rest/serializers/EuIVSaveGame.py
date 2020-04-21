from rest_framework import serializers

from EUIVSaveGame.models import EuIVSaveGame


class EuIVSaveGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = EuIVSaveGame
        fields = '__all__'


class EuIVSimpleSaveGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = EuIVSaveGame
        fields = ['savegame_name', 'savegame_date', 'savegame_lines', 'savegame_is_multi_player', 'active']
