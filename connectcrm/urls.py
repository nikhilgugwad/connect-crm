"""
URL configuration for the ConnectCRM project.

This file routes incoming requests to appropriate views and APIs. The root URL (`/`) will show a welcome message, while the `/api/` endpoint includes all API-related routes from the 'api' app.

It serves as the central place where different URL patterns are registered, and it defines the application's entry points for the admin panel, root view, and API endpoints.
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple view for the root URL
def home(request):
    """
    Home view that returns a welcome message for the ConnectCRM API.
    This is a simple view that will be shown when the user accesses the root URL (e.g., http://localhost:8000/).

    Returns:
        HttpResponse: A response containing a welcome message.
    """
    return HttpResponse("Welcome to the ConnectCRM API!")

urlpatterns = [
    # Admin panel URL (accessible by /admin/)
    path('admin/', admin.site.urls),
    
    # Root URL that returns a welcome message
    path('', home),  # This will show "Welcome to the ConnectCRM API!" at the root URL
    
    # API endpoints (all URLs starting with /api/ will be handled by the 'api.urls' module)
    path('api/', include('api.urls')),  # Includes the URLs defined in the 'api' app
]
