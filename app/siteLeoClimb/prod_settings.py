import dj_database_url
from siteLeoClimb.settings import *

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['leoclimb.herokuapp.com','leoclimb.fr','www.leoclimb.fr']

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

#SECURE_SSL_REDIRECT = True
