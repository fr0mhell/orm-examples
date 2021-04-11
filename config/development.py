from .common import *

DEBUG = True
if 'celery' in sys.argv[0]:
    DEBUG = False

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

SECRET_KEY = '5_wteua^80be^ku_3h2#n33)i%2@)uu*lamy4(xsxb4^n*piy!'

# Any host allowed
ALLOWED_HOSTS = ['*']

# Celery config
CELERY_BROKER_URL = 'redis://redis:6379/1'
CELERY_RESULT_BACKEND = 'redis://redis:6379/1'
CELERY_TASK_ALWAYS_EAGER = False
