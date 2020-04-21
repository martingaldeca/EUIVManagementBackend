# Generated by Django 3.0.5 on 2020-04-13 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EUIVSaveGame', '0002_euivsavegame_host_user'),
        ('EUIVCountries', '0005_euivcountry_color'),
        ('EUIVStats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EuIVCountryStats',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Datetime when de object was created.', null=True, verbose_name='Creation datetime')),
                ('modification_datetime', models.DateTimeField(auto_now=True, db_index=True, help_text='Datetime of the last object modification.', null=True, verbose_name='Modification datetime')),
                ('stats_date', models.DateField(blank=True, db_index=True, help_text='Current date in the savegame when the screenshot.', null=True, verbose_name='Stats date')),
                ('country', models.ForeignKey(blank=True, help_text='Current country for the info.', null=True, on_delete=django.db.models.deletion.CASCADE, to='EUIVCountries.EuIVCountry', verbose_name='Country')),
                ('save_game', models.ForeignKey(blank=True, help_text='Save game associated to the country info.', null=True, on_delete=django.db.models.deletion.CASCADE, to='EUIVSaveGame.EuIVSaveGame', verbose_name='Save game')),
            ],
            options={
                'verbose_name': 'Country stat',
            },
        ),
    ]