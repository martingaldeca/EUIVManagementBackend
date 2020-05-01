from django.db import models
from django.db.models.functions import datetime


class EuIVModel(models.Model):
    id = models.AutoField(primary_key=True)
    creation_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True, db_index=True, verbose_name='Creation datetime', help_text='Datetime when de object was created.')
    modification_datetime = models.DateTimeField(auto_now=True, null=True, blank=True, db_index=True, verbose_name='Modification datetime', help_text='Datetime of the last object modification.')

    def save(self, force_save: bool = False, *args, **kwargs):
        """
        Overwrite save to see update the last modification datetime.
        :param force_save:
        :param args:
        :param kwargs:
        :return:
        """
        self.modification_datetime = datetime.timezone.now()
        self.control_in_save(force_save)
        return super(EuIVModel, self).save(*args, **kwargs)

    def control_in_save(self, force_save: bool = False, **kwargs):
        """
        Each model will overwrite this method if it just need to check any specific condition or logic on save
        :param force_save:
        :param kwargs:
        :return:
        """
        pass

    class Meta:
        abstract = True
