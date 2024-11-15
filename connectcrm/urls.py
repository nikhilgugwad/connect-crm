# connectcrm/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple view for the root URL
def home(request):
    return HttpResponse("Welcome to the ConnectCRM API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # This will show "Welcome to the ConnectCRM API!" at the root URL
    path('api/', include('api.urls')),  # Include the api urls here
]
