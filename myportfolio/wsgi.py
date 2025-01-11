"""
WSGI config for myportfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Obtener el entorno desde la variable de entorno o usar 'produccion' como predeterminado
DJANGO_ENV = os.getenv('DJANGO_ENV', 'produccion')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'myportfolio.settings.{DJANGO_ENV}')

application = get_wsgi_application()

