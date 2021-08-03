from .base import *
import os

# Secret key
SECRET_KEY = 'django-insecure-2@je&3s47ffy8ph&k*8l=%ep*8mn0rj0_-b)e9r4ij=j%hqee-'

# Debug in development
DEBUG = True
ALLOWED_HOSTS = []

# Site ID
SITE_ID = 2

# Local database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'orbit',
        'USER': 'orbit',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Static URL and DIR
STATIC_URL = '/static/'

# Media Files local
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Local recaptcha
GOOGLE_RECAPTCHA_SECRET_KEY = '6LeleRAaAAAAAEHqQzug3vmGBNg1L605fHS8XYyt'

# Local SMTP Configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ajaychoudhury1221@gmail.com'
EMAIL_HOST_PASSWORD = 'anunami@123'
