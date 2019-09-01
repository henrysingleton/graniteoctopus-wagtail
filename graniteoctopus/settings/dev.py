from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*p15w7sp-72w@=^09zgib8i9mw=2n_&n@=d(_vkp%dan(&_noz'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

ALLOWED_HOSTS = [
    'localhost',
    'local.henrysingleton.com'
]

INTERNAL_IPS = [
    '127.0.0.1',
    '0.0.0.0',
    '172.20.0.1'
]