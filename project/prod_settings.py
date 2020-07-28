""" Production Settings """
import dj_database_url

from .settings import *


############
# SECURITY #
############

DEBUG = False

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)

ALLOWED_HOSTS = ['ideally-app.herokuapp.com']

# production email backend using sendgrid
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_API_KEY')
EMAIL_USE_SSL = True
