from .base import *

secrets = json.load(open(os.path.join(SECRET_ROOT, 'dev.json')))

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = secrets['DATABASES']

ALLOWED_HOSTS = secrets['ALLOWED_HOSTS']

DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'

AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'
