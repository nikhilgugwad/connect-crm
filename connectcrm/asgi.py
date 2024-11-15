import os
from django.core.asgi import get_asgi_application

# Set the default Django settings module for the 'asgi' application.
# This will allow Django to know which settings to use.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connectcrm.settings')

# Create the ASGI application instance.
# This function returns the ASGI application callable which will be used by the server to interact with Django.
application = get_asgi_application()
