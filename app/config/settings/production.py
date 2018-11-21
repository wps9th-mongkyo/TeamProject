from .base import *

secrets = json.load(open(os.path.join(SECRET_ROOT, 'production.json')))

WSGI_APPLICATION = 'config.wsgi.production.application'

DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'

DATABASES = secrets['DATABASES']
