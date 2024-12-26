from pathlib import Path
import os
from azure.storage.blob import BlobServiceClient, ContainerClient


AZURE_ACCOUNT_NAME = 'ulfs202312'
AZURE_ACCOUNT_KEY = 'dLeqjRgdpuFn6ui7RKP4p3qS5qTxR+hVUkr/5hpU1rQnJve9IEuz76aW4rH+EOBm1JP+8URJTT+n+AStoUApwA=='
AZURE_CONTAINER = 'static'  # The container where files will be stored

DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

AZURE_STORAGE_CONNECTION_STRING = f"DefaultEndpointsProtocol=https;AccountName={AZURE_ACCOUNT_NAME};AccountKey={AZURE_ACCOUNT_KEY};EndpointSuffix=core.windows.net"
AZURE_LOCATION = 'eastus2'  # e.g., 'westus'
AZURE_SSL = True
STATICFILES_STORAGE = 'storages.backends.azure_storage.AzureStorage'
STATIC_ROOT = '/static/'
STATIC_URL = f"https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/{AZURE_CONTAINER}/"


DB_NAME='ulfs'
DB_SERVER = 'ulfs-info5900.database.windows.net'
DB_USER_NAME = 'ulfs'
DB_PASSWORD = 'MacBook@1993'

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-ll6d476=!s9zvba-gm+gae)-p%!ix8b)zhasegh_s*2m+g9c!='

DEBUG = True

ALLOWED_HOSTS = ["ulfs.azurewebsites.net", "*"]
CSRF_TRUSTED_ORIGINS = ['https://*.azurewebsites.net','https://*.127.0.0.1']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ulfs202312@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'ejkl dzij lxia myjh'  # Your Gmail App Password



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'main',
    'storages',
    'sa'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ulfs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = 'ulfs.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': DB_NAME,
        'USER': DB_USER_NAME,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_SERVER,
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_TZ = True


# STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# MEDIA_URL = f"https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/media/"
# MEDIA_ROOT = f"https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
