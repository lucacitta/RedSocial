from .base import *
from .password import PASSWORD_PASSWORD

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'RedSocial',
        'USER': 'postgres',
        'PASSWORD': PASSWORD_PASSWORD,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

