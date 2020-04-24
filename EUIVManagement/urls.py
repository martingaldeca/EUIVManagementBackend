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
from django.conf.urls.static import static
from .settings import MEDIA_URL, MEDIA_ROOT
from EUIVManagement.rest.views import EuIVPlatformInfo
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('', admin.site.urls),

    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^api/auth/refresh_token/', refresh_jwt_token),

    # EUIVManagement api
    path('api/', include('EUIVStats.urls')),
    path('api/', include('EUIVCountries.urls')),
    path('api/', include('EUIVSaveGame.urls')),
    path('api/', include('EUIVUserManagement.urls')),

    path('api/platform_info', EuIVPlatformInfo.as_view(), name='database_info'),

]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
