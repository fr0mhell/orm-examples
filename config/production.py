from .common import *

PROJECT_ENV = 'production'

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5_wteua^80be^ku_3h2#n33)i%2@)uu*lamy4(xsxb4^n*piy!'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prod_db',
        'USER': 'prod_user',
        'PASSWORD': 'prod_pwd',
        'HOST': 'db-prod',
        'PORT': 5432,
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
    }
}

# Celery config
CELERY_BROKER_URL = 'redis://redis:6379/1'
CELERY_RESULT_BACKEND = 'redis://redis:6379/1'
