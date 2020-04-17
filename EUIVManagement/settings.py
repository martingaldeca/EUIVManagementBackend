"""
Django settings for EUIVManagement project.
"""

import os
from EUIVManagement.django_settings import *

SECRET_KEY = '$6edr%_r!^hpzne0mg+!f9l4ke6z0r3=8smh3yxb=+4j*vr1(*'
DEBUG = True
ALLOWED_HOSTS = ['*']
WSGI_APPLICATION = 'EUIVManagement.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = "/static/"
MEDIA_ROOT = "/media/"

# Redefine the auth user model
AUTH_USER_MODEL = 'EUIVUserManagement.EuIVUser'
