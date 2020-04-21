from rest_framework import serializers
from EUIVCountries.rest.serializers import EuIVProvinceSerializer, EuIVCountrySerializer
from EUIVSaveGame.rest.serializers import EuIVSaveGameSerializer
from EUIVStats.models import EuIVProvinceStats


class EuIVProvinceStatsSerializer(serializers.ModelSerializer):

    province = EuIVProvinceSerializer(many=False, read_only=False)
    owner = EuIVCountrySerializer(many=False, read_only=False)
    controller = EuIVCountrySerializer(many=False, read_only=False)
    save_game = EuIVSaveGameSerializer(many=False, read_only=False)

    class Meta:
        model = EuIVProvinceStats
        fields = '__all__'
