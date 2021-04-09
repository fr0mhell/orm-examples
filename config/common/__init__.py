from .auth import *
from .database import *
from .installed_apps import *
from .internationalization import *
from .logging import *
from .middleware import *
from .paths import *
from .rest_framework import *
from .static import *
from .templates import *


SITE_ID = 1

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

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
