from rest_framework import serializers

from EUIVStats.models import EuIVProvinceStats


class EuIVProvinceStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EuIVProvinceStats
        fields = '__all__'
