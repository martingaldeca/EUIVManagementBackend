from rest_framework import serializers

from EUIVCountries.models import EuIVCountry


class EuIVCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EuIVCountry
        fields = '__all__'

