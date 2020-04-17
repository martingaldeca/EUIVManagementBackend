from django.urls import path

from EUIVCountries.rest.views import EuIVProvinceList

urlpatterns = [
    path('provinces/', EuIVProvinceList.as_view(), name='list_provinces'),
]
