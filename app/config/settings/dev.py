from .base import *

secrets = json.load(open(os.path.join(SECRET_ROOT, 'dev.json')))

WSGI_APPLICATION = 'config.wsgi.dev.application'

DATABASES = secrets['DATABASES']

ALLOWED_HOSTS = secrets['ALLOWED_HOSTS']

DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

AWS_ACCESS_KEY_ID = secrets['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secrets['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'