"""
WSGI configuration for the ConnectCRM project.

This file serves as the entry point for WSGI-compatible web servers to run the Django application.

It exposes the WSGI callable as a module-level variable named ``application`` that can be used by web servers for handling requests.

For more information on WSGI, see:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'connectcrm' project.
# This is used by WSGI servers to know which Django settings to load.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connectcrm.settings')

# Get the WSGI application for the Django project.
# This callable will be used by WSGI-compatible servers (e.g., Gunicorn) to handle requests.
application = get_wsgi_application()
