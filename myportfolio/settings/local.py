from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

INSTALLED_APPS += ['django_browser_reload']
MIDDLEWARE += ['django_browser_reload.middleware.BrowserReloadMiddleware']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '5432',
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]
