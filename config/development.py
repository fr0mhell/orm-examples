from .common import *

DEBUG = True

PROJECT_ENV = 'development'

INSTALLED_APPS += [
    'debug_toolbar',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dev_db',
        'USER': 'dev_user',
        'PASSWORD': 'dev_pwd',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

CACHES = {
    'default': {
        # 'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
    }
}

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

SECRET_KEY = '5_wteua^80be^ku_3h2#n33)i%2@)uu*lamy4(xsxb4^n*piy!'

# Any host allowed
ALLOWED_HOSTS = ['*']
