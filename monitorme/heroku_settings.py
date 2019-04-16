from monitorme.settings import *

import django_heroku 

	
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '0.0.0.0',
]

django_heroku.settings(locals())