from django.db import models
from EUIVManagement.helpers import EuIVModel
from EUIVSaveGame.models import EuIVSaveGame
from EUIVCountries.models import EuIVProvince, EuIVCountry


class EuIVProvinceStats(EuIVModel):
    # Basic info of the stat
    save_game = models.ForeignKey(EuIVSaveGame, null=True, blank=True, verbose_name='Save game', help_text='Save game associated to the province info.', on_delete=models.CASCADE, db_index=True)
    stats_date = models.DateField(auto_now=False, blank=True, null=True, verbose_name='Stats date', help_text='Current date in the savegame when the screenshot.', db_index=True)
    province = models.ForeignKey(EuIVProvince, null=True, blank=True, verbose_name='Province', help_text='Current province for the info.', on_delete=models.CASCADE, db_index=True)

    # Custom info for the province
    development = models.FloatField(blank=True, null=True, verbose_name='Development', help_text='Current development of the province.')
    base_tax = models.FloatField(blank=True, null=True, verbose_name='Base Tax', help_text='Current base tax of the province.')
    base_production = models.FloatField(blank=True, null=True, verbose_name='Base production', help_text='Current base production of the province.')
    base_manpower = models.FloatField(blank=True, null=True, verbose_name='Base manpower', help_text='Current base manpower of the province.')
    trade_power = models.FloatField(blank=True, null=True, verbose_name='Trade power', help_text='Current trade power of the province.')
    owner = models.ForeignKey(EuIVCountry, blank=True, null=True, verbose_name='Owner', help_text='Current owner of the province.', on_delete=models.CASCADE, related_name='province_owner')
    controller = models.ForeignKey(EuIVCountry, blank=True, null=True, verbose_name='Controller', help_text='Current controller of the province.', on_delete=models.CASCADE, related_name='province_controller')
    devastation = models.FloatField(blank=True, null=True, verbose_name='Devastation', help_text='Current devastation of the province.')

    class Meta:
        verbose_name = 'Province stat'

    def __str__(self):
        return f'Stats for {self.save_game} - {self.province} - {self.stats_date}'
