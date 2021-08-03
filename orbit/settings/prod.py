from .base import *
import os

# Secret key
SECRET_KEY = 'django-insecure-2@je&3s47ffy8ph&k*8l=%ep*8mn0rj0_-b)e9r4ij=j%hqee-'

# Debug in production
DEBUG = False
ALLOWED_HOSTS = ['67.207.82.73', 'localhost']

# Installed apps
INSTALLED_APPS += [
    'storages',
]

# Site ID
SITE_ID = 2

# Production database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'orbitgadget',
        'USER': 'ajay',
        'PASSWORD': 'Gothicstyle@2',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Static and media files on custom storage
AWS_ACCESS_KEY_ID = 'E3M52LQ2CERSXGXVL4EC'
AWS_SECRET_ACCESS_KEY = 'kE794GPhYLHK3xWBEZ0Et4UqGZC3mT8eioFALf3yRLo'
AWS_STORAGE_BUCKET_NAME = 'orbitapi'
AWS_S3_ENDPOINT_URL = 'https://orbitapi.nyc3.digitaloceanspaces.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_DEFAULT_ACL = 'public-read'
AWS_S3_SIGNATURE_VERSION = 's3v4'

# Static and media URL
STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, 'staticfiles')
MEDIA_URL =  'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, 'mediafiles')

# Storage
STATICFILES_STORAGE =  'custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

# Production recaptcha
GOOGLE_RECAPTCHA_SECRET_KEY = '6LeleRAaAAAAAEHqQzug3vmGBNg1L605fHS8XYyt'

# Production SMTP Configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ajaychoudhury1221@gmail.com'
EMAIL_HOST_PASSWORD = 'anunami@123'
