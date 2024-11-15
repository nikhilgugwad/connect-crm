from django.apps import AppConfig

class ApiConfig(AppConfig):
    """
    Configuration for the 'api' application.

    This class is used by Django to configure the 'api' app. It allows us to set app-specific
    configurations such as the default auto field type. The 'name' attribute tells Django the
    name of the application, which is used for app discovery and other configuration purposes.
    """
    
    # Setting the default primary key field type for models in this app.
    default_auto_field = 'django.db.models.BigAutoField'
    
    # The name of the app. Django uses this to identify and register the app.
    name = 'api'
