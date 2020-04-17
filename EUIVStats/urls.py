from django.urls import path

from EUIVStats.rest.views import EuIVProvinceStatsList

urlpatterns = [
    path('province_stats/', EuIVProvinceStatsList.as_view(), name='list_province_stats'),
]
