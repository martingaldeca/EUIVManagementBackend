from django.db import models
from django.db.models.functions import datetime


class EuIVModel(models.Model):
    id = models.AutoField(primary_key=True)
    creation_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True, db_index=True, verbose_name='Creation datetime', help_text='Datetime when de object was created.')
    modification_datetime = models.DateTimeField(auto_now=True, null=True, blank=True, db_index=True, verbose_name='Modification datetime', help_text='Datetime of the last object modification.')

    def save(self, *args, **kwargs):
        """
        Overwrite save to see update the last modification datetime.
        :param args:
        :param kwargs:
        :return:
        """
        self.modification_datetime = datetime.timezone.now()
        return super(EuIVModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
