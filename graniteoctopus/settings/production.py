from .base import *

DEBUG = False
TEMPLATE_DEBUG = False
SECRET_KEY = '' #Remember to change this.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'graniteoctopus',
        'USER': 'graniteoctopus',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = [
    'graniteoctopus.com'
]

try:
    from .local import *
except ImportError:
    pass
