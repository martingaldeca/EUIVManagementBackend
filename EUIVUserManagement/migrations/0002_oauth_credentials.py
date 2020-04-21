from django.db import migrations
import os
from oauth2_provider.models import Application
from EUIVUserManagement.models import EuIVUser, EuIVUserTypes
from logging import getLogger

logger = getLogger(__name__)


def create_default_oauth_app(apps, schema_editor):
    """
    Function to create teh default permission for the api.

    The default values for the API will be provided by env variables.

    If this is in production the variables of the .env file should be overwritten.
    :param apps:
    :param schema_editor:
    :return:
    """
    client_id = os.getenv('OAUTHCLIENTID')
    client_secret = os.getenv('OAUTHCLIENTSECRET')

    if client_id is None:
        logger.warning('The environment variable OAUTHCLIENTID is not set. The default value will be set as value.')
        client_id = 'FFCm36ebjlg3PTmPFdhhea4wWVD'
    if client_secret is None:
        logger.warning('The environment variable OAUTHCLIENTSECRET is not set. The default value will be set as value.')
        client_secret = 'BTK3nLW862n4xPIh8iXCnQy8ZonPLJWj4BqnpeqnmY52xrpb'

    # Create the admin default user
    # This user should change the password by default first time enter in the application
    user, created = EuIVUser.objects.get_or_create(username='admin', user_type=EuIVUserTypes.admin, is_staff=True, is_superuser=True, is_active=True)
    default_application_password = 'root1234'
    if created:
        logger.info(f'The default password for admin user will be {default_application_password}.')
        user.set_password(default_application_password)
    user.save()

    # Create the default application oauth settings
    Application(client_id=client_id, client_secret=client_secret, client_type="confidential", authorization_grant_type="password", name="EUIVManagement", user=user).save()


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('EUIVUserManagement', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_oauth_app)
    ]
