"""
Django settings for EUIVManagement project.
"""

import os
from datetime import timedelta

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

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('JWT',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}
