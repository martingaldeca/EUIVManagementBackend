# Generated by Django 3.0.5 on 2020-04-12 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('EUIVSaveGame', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='euivsavegame',
            name='host_user',
            field=models.ForeignKey(blank=True, help_text='The host of the savegame.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Host user'),
        ),
    ]
