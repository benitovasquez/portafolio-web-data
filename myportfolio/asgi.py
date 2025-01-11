"""
ASGI config for myportfolio project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Obtener el entorno desde la variable de entorno o usar 'produccion' como predeterminado
DJANGO_ENV = os.getenv('DJANGO_ENV', 'produccion')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"myportfolio.settings.{DJANGO_ENV}")

application = get_asgi_application()
