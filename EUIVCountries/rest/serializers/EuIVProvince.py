from rest_framework import serializers

from EUIVCountries.models import EuIVProvince


class EuIVProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EuIVProvince
        fields = '__all__'
