"""
Django settings for the connectcrm project.

This file contains configuration settings for the Django application, including:
- Installed apps
- Middleware
- Database configuration
- Static files settings
- Security settings

This configuration file is essential for the correct operation of the Django app in both development and production environments.
"""

from pathlib import Path
import os
from decouple import config  # To load sensitive information from environment variables

# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: Keep the secret key used in production secret!
# The secret key is loaded from environment variables for security.
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: Don't run with DEBUG turned on in production!
DEBUG = False  # In production, debug should be False to avoid security risks.

# Define allowed hosts for security.
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'connectcrm-bb1693933592.herokuapp.com',  # Heroku hostname
]

# Application definition
INSTALLED_APPS = [
    # Django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',  # For building APIs
    'rest_framework.authtoken',  # For token-based authentication (optional, if needed)
    'drf_yasg',  # For Swagger API documentation
    'rest_framework_simplejwt',  # For JWT-based authentication
    
    # Custom app
    'api',  # The custom application where models, views, and serializers are defined
    
    # For handling static files and CORS (Cross-Origin Resource Sharing)
    'whitenoise.runserver_nostatic',  # For serving static files in production
    'corsheaders',  # For handling CORS in development and production
]

MIDDLEWARE = [
    # Security middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Static file handling and CORS
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise for serving static files
    'corsheaders.middleware.CorsMiddleware',  # Handles CORS for the app
]

# Root URL configuration
ROOT_URLCONF = 'connectcrm.urls'

# Template configuration (not used in this project but can be enabled if needed)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add custom template directories here if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application (not used for ASGI servers but included in case WSGI is needed)
WSGI_APPLICATION = 'connectcrm.wsgi.application'

# Database configuration
# The database settings are loaded from environment variables for security.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),  # Loaded from environment variable
        'USER': config('DB_USER'),  # Loaded from environment variable
        'PASSWORD': config('DB_PASSWORD'),  # Loaded from environment variable
        'HOST': config('DB_HOST'),  # Loaded from environment variable
        'PORT': config('DB_PORT', default='3306'),  # Default MySQL port
    }
}

# Password validation settings (use Django's default password validators)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization settings
LANGUAGE_CODE = 'en-us'  # Language for the application
TIME_ZONE = 'UTC'  # Time zone for the application

USE_I18N = True  # Internationalization enabled
USE_TZ = True  # Time zone support enabled

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'  # URL prefix for serving static files

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User model
AUTH_USER_MODEL = 'api.CustomUser'

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT-based authentication
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Ensure user is authenticated
    ],
}

# Static files storage settings (WhiteNoise for serving static files in production)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# CORS (Cross-Origin Resource Sharing) settings
CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins for development (adjust in production)
