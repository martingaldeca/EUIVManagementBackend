from django.db import models
from ast import literal_eval
from EUIVManagement.helpers import EuIVModel


class EuIVCountry(EuIVModel):
    tag = models.CharField(max_length=6, db_index=True, blank=False, null=False, verbose_name='Country tag', help_text='Internal EUIV tag for countries.', unique=True)
    name = models.CharField(max_length=50, db_index=True, blank=True, null=True, verbose_name='Country name', help_text='Complete name of the country', default='Country')
    color = models.CharField(max_length=19, blank=True, null=True, verbose_name='Country color', help_text='Color of the country in RGB way with comma separator (000, 000, 000)', default='000, 000, 000')

    def __str__(self):
        return f"{self.tag} - {self.name}"

    def get_color(self):
        """
        Function to return the rgb color
        :return:
        """
        return literal_eval(self.color)

    class Meta:
        verbose_name = 'Countrie'
