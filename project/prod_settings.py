""" Production Settings """
from .settings import *


############
# SECURITY #
############

DEBUG = True

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)

ALLOWED_HOSTS = ['ideally-app.herokuapp.com']
