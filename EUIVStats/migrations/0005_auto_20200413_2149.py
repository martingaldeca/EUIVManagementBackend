# Generated by Django 3.0.5 on 2020-04-13 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EUIVStats', '0004_auto_20200413_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='euivcountrystats',
            name='government',
            field=models.CharField(blank=True, help_text='Current government of the country.', max_length=50, null=True, verbose_name='Government'),
        ),
    ]