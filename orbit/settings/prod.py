from .base import *
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Secret key
# with open('/home/ajay/secret_key.txt') as f:
#     SECRET_KEY = f.read().strip()
SECRET_KEY = 'django-insecure-2@je&3s47ffy8ph&k*8l=%ep*8mn0rj0_-b)e9r4ij=j%hqee-'

# Debug in production
DEBUG = True
# DEBUG = False
ALLOWED_HOSTS = ['chrysalisiiserb.herokuapp.com', 'localhost', '127.0.0.1']

# Site ID
SITE_ID = 2

# ie if Heroku server
if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config()}

# Static and media URL
STATIC_URL = '/static/'
MEDIA_URL =  '/media/'


# Production recaptcha
# with open('/home/ajay/recaptcha_key.txt') as g:
GOOGLE_RECAPTCHA_SECRET_KEY = "6LdTlgEfAAAAAO4Df_xQrqQG013LHxHhYEPetLug"

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

# adding config
cloudinary.config( 
  cloud_name = "chrysalis-iiserb", 
  api_key = "425627182992517", 
  api_secret = "aJ6pgggY4wWqiL7Bmmngtb-LesU" 
)