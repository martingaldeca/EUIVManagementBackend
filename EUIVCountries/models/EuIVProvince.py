from django.db import models
from EUIVManagement.helpers import EuIVModel


class EuIVProvince(EuIVModel):
    identifier = models.CharField(max_length=6, db_index=True, blank=False, null=False, verbose_name='Province identifier', help_text='Internal EUIV identifier for provinces.', unique=True)
    name = models.CharField(max_length=50, db_index=True, blank=True, null=True, verbose_name='Province name', help_text='Complete name of the province', default='Province')

    def __str__(self):
        return f"{self.identifier} - {self.name}"

    class Meta:
        verbose_name = 'Province'
