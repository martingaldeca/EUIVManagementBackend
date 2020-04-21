"""EUIVManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from EUIVManagement.rest.views import EuIVPlatformInfo

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('', admin.site.urls),

    path('api/auth/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # EUIVManagement api
    path('api/', include('EUIVStats.urls')),
    path('api/', include('EUIVCountries.urls')),
    path('api/', include('EUIVSaveGame.urls')),

    path('api/platform_info', EuIVPlatformInfo.as_view(), name='database_info'),

]
