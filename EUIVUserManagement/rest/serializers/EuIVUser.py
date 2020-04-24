from rest_framework import serializers
from EUIVUserManagement.models import EuIVUser, EuIVUserProfile, EuIVUserTypes, EuIVUserActiveGames


class EuIVUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EuIVUser
        fields = ['id', 'last_login', 'is_superuser', 'username', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined']



class EuIVUserProfileSerializer(serializers.ModelSerializer):
    user = EuIVUserSerializer(many=False, read_only=False)

    class Meta:
        model = EuIVUserProfile
        fields = '__all__'


class EuIVSimpleUserProfileSerializer(serializers.ModelSerializer):

    user_type = serializers.SerializerMethodField('get_user_type')
    username = serializers.SerializerMethodField('get_username')
    email = serializers.SerializerMethodField('get_email')
    total_games = serializers.SerializerMethodField('get_total_games')

    class Meta:
        model = EuIVUserProfile
        fields = ['user_type', 'username', 'user', 'email', 'total_games']

    @staticmethod
    def get_user_type(obj):
        return EuIVUserTypes.attributes[obj.user_type]

    @staticmethod
    def get_username(obj):
        return obj.user.username

    @staticmethod
    def get_email(obj):
        return obj.user.email

    @staticmethod
    def get_total_games(obj):
        return EuIVUserActiveGames.objects.filter(user=obj.user).count()
