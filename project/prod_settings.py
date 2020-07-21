""" Production Settings """
import dj_database_url

from .settings import *


############
# SECURITY #
############

# TODO: turn off for real production
DEBUG = True

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)

ALLOWED_HOSTS = ['ideally-app.herokuapp.com']
