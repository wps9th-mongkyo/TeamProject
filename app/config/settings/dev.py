from .base import *

secrets = json.load(open(os.path.join(SECRET_ROOT, 'dev.json')))

WSGI_APPLICATION = 'config.wsgi.application'

DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'


ALLOWED_HOSTS = secrets['ALLOWED_HOSTS']

