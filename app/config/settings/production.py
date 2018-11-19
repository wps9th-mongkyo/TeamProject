from .base import *


WSGI_APPLICATION = 'config.wsgi.production.application'

DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
