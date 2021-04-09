import sys

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
]

LOCAL_APPS = [
    'space_rangers',
    'emails',
]

# reduce number of apps for celery
IN_CELERY = False
if 'celery' in sys.argv[0]:
    IN_CELERY = True

# Django backend launched
if not IN_CELERY:
    INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS
else:
    INSTALLED_APPS = LOCAL_APPS
