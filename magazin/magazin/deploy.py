"""
WSGI config for magazin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

path = "/home/dmitrygorbachev/deploy_python/"
if path not in sys.path:
    sys.path.append(path)


path = "/home/dmitrygorbachev/deploy_python/"
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "magazin.settings")

from django.core.wsgi import get_wsgi_application

from whitenoise.django import DjangoWhiteNoise


application = get_wsgi_application()
application = DjangoWhiteNoise(application)
