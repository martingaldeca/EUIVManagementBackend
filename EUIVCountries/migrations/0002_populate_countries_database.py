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
        counter = 0
        for row in csv_reader:
            counter += 1
            euiv_country(
                tag=row['Tag'],
                name=row['Name']
            ).save()
    countries_file.close()
    logger.info(f"The migration populates the countries database with {counter} countries.")


class Migration(migrations.Migration):
    dependencies = [
        ('EUIVCountries', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_countries)
    ]
