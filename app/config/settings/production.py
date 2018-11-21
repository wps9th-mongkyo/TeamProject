from .base import *


WSGI_APPLICATION = 'config.wsgi.production.application'

DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'

DATABASES = secrets['DATABASES']
