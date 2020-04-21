from django.urls import path

from EUIVCountries.rest.views import EuIVProvinceList, EuIVCountryList

urlpatterns = [
    path('provinces/', EuIVProvinceList.as_view(), name='list_provinces'),
    path('countries/', EuIVCountryList.as_view(), name='list_countries'),
]
