from .base import *
import os

# Secret key
# with open('/home/ajay/secret_key.txt') as f:
#     SECRET_KEY = f.read().strip()
# SECRET_KEY = 'django-insecure-2@je&3s47ffy8ph&k*8l=%ep*8mn0rj0_-b)e9r4ij=j%hqee-'

# Debug in production
DEBUG = True
# DEBUG = False
ALLOWED_HOSTS = ['chrysalisiiserb.herokuapp.com', 'localhost', '127.0.0.1']

# Site ID
SITE_ID = 2

# Production database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static and media files

# Static and media URL
STATIC_URL = '/static/'
MEDIA_URL =  '/media/'


# Production recaptcha
# with open('/home/ajay/recaptcha_key.txt') as g:
#     GOOGLE_RECAPTCHA_SECRET_KEY = g.read().strip()

# Production SMTP Configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'orbitgadget@gmail.com'

# with open('/home/ajay/email_pass.txt') as h:
#     EMAIL_HOST_PASSWORD = h.read().strip()

# # HTTPS settings
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

# # HSTS settings
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

import django_heroku
django_heroku.settings(locals())