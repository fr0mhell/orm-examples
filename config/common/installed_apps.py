THIRD_PARTY_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework.authentication',
    'allauth',
    'allauth.account',
    'django_filters',
    'drf_yasg',
    'dj_rest_auth',
]

LOCAL_APPS = [
    'space_rangers',
    'emails',
]

INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS
