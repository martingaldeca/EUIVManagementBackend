INTERNAL_APPS = [
    'EUIVSaveGame',
    'EUIVUserManagement',
    'EUIVCountries',
    'EUIVStats',
]

EXTERNAL_LIBRARIES = [
    'simple_history',
    'debug_toolbar',
    'django_extensions',
    'corsheaders',
    'oauth2_provider',
    'rest_framework',
]

INSTALLED_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + INTERNAL_APPS + EXTERNAL_LIBRARIES
