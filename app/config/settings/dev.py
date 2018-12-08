from .base import *

DEBUG = True

dev_secrets = json.load(open(os.path.join(SECRET_ROOT, 'dev.json')))

WSGI_APPLICATION = 'config.wsgi.dev.application'

DATABASES = dev_secrets['DATABASES']

ALLOWED_HOSTS = dev_secrets['ALLOWED_HOSTS']

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
