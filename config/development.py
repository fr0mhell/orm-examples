from .common import *

DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5_wteua^80be^ku_3h2#n33)i%2@)uu*lamy4(xsxb4^n*piy!'

# Any host allowed
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': f'{BASE_DIR}/db.sqlite3',
    }
}
