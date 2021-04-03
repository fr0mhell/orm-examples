from .common import *

DEBUG = False

SITE_ID = 1

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5_wteua^80be^ku_3h2#n33)i%2@)uu*lamy4(xsxb4^n*piy!'

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres_db',
        'USER': 'postgres_user',
        'PASSWORD': 'postgres_pwd',
        'HOST': 'postgres',
        'PORT': 5432,
    }
}

# Shell Plus additional imports
SHELL_PLUS = 'ipython'
# loading of factories in shell_plus
SHELL_PLUS_PRE_IMPORTS = [
    'from space_rangers.factories import *',
]

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_FROM = 'no-reply@spaceships.com'

INTERNAL_IPS = [
    '127.0.0.1',
    '0.0.0.0',
]
