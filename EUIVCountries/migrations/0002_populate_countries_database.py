from django.db import migrations, models
from logging import getLogger
import csv

logger = getLogger(__name__)


def create_default_countries(apps, schema_editor):
    """
    Function to populate the countries database
    :param apps:
    :param schema_editor:
    :return:
    """
    euiv_country = apps.get_model("EUIVCountries", "EuIVCountry")
    with open('EUIVCountries/countries.csv') as countries_file:
        csv_reader = csv.DictReader(countries_file)
        for row in csv_reader:
            country_to_save, created = euiv_country.objects.get_or_create(tag=row['Tag'])
            country_to_save.name = row['Name']
            country_to_save.save()
    countries_file.close()


class Migration(migrations.Migration):
    dependencies = [
        ('EUIVCountries', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_countries)
    ]
