from django.contrib import admin

from .models import EuIVCountry, EuIVProvince


@admin.register(EuIVCountry)
class EuIVCountryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'tag',
        'name',
    )
    readonly_fields = 'creation_datetime', 'modification_datetime'
    list_filter = ('creation_datetime', 'modification_datetime', 'name', 'tag')
    search_fields = ('name', 'tag')


@admin.register(EuIVProvince)
class EuIVProvinceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'identifier',
        'name',
    )
    readonly_fields = 'creation_datetime', 'modification_datetime'
    list_filter = ('creation_datetime', 'modification_datetime', 'name', 'identifier')
    search_fields = ('name', 'identifier')
