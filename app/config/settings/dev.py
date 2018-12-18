from .base import *

DEBUG = True

dev_secrets = json.load(open(os.path.join(SECRET_ROOT, 'dev.json')))

WSGI_APPLICATION = 'config.wsgi.dev.application'

DATABASES = dev_secrets['DATABASES']

ALLOWED_HOSTS = dev_secrets['ALLOWED_HOSTS']

# production settings 설정 가져오기
# prod_secrets = json.load(open(os.path.join(SECRET_ROOT, 'production.json')))
# DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
# # collectstatic을 실행했을 때,
# # 버킷의 'static'폴더 아래에 정적파일들이 저장되도록 설정해보기
# #  config.storages.StaticStorage클래스를 만들어서 적용
# # STATICFILES_STORAGE = 'config.storages.StaticStorage'
# # 위 설정시 S3 프리티어의 기본 PUT한계를 금방 초과하게되므로
# #  STATIC_ROOT에 collectstatic후 Nginx에서 제공하는 형태로 사용
#
# AWS_ACCESS_KEY_ID = prod_secrets['AWS_ACCESS_KEY_ID']
# AWS_SECRET_ACCESS_KEY = prod_secrets['AWS_SECRET_ACCESS_KEY']
# AWS_STORAGE_BUCKET_NAME = prod_secrets['AWS_STORAGE_BUCKET_NAME']
# AWS_S3_SIGNATURE_VERSION = 's3v4'
# AWS_S3_REGION_NAME = 'ap-northeast-2'


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
