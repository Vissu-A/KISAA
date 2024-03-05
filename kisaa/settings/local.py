from .base import *
from decouple import config, Csv
from kombu.utils.url import safequote

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('local_debug', cast = bool)

ALLOWED_HOSTS = config('local_allowed_hosts', cast = Csv())

DATABASES = {
    "default": {
        "ENGINE": config('local_db_engine'),
        "NAME": config('local_db_name'),
    }
}

# Celery settings
aws_access_key_id = safequote(config('local_celery_broker_aws_sqs_access_key_id'))
aws_secret_key = safequote(config('local_celery_broker_aws_sqs_secret_access_key'))
broker_url = f"sqs://{aws_access_key_id}:{aws_secret_key}@"

CELERY_BROKER_URL = broker_url
CELERY_RESULT_BACKEND = config('local_celery_result_backend')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'
# broker_transport = "sqs"
# broker_transport_options= {
#     "region": "us-east-1",
#     'max_retries': 3,
#     "polling_interval": 20,
#     'visibility_timeout': 40,
#     'queue_name_prefix': 'kisaa-celery-',
# }

# Email settings
EMAIL_BACKEND = config('local_email_backend')
EMAIL_HOST = config('local_email_host')
EMAIL_PORT = config('local_email_port')
EMAIL_HOST_USER = config('local_email_host_user')
EMAIL_HOST_PASSWORD = config('local_email_host_passcode')
EMAIL_USE_TLS = True    # 587
EMAIL_USE_SSL = False   # 465

# S3 Bucket file upload settings
AWS_ACCESS_KEY_ID = config('local_aws_access_key_id')
AWS_SECRET_ACCESS_KEY = config('local_aws_secret_access_key')
AWS_STORAGE_BUCKET_NAME = config('local_aws_storage_bucket_name')
DEFAULT_FILE_STORAGE = config('local_default_file_storage')
# ACL means Access Control List. by default inherits the bucket permissions.
AWS_DEFAULT_ACL = config('local_aws_default_acl')
# By default files with the same name will overwrite each other.True by default.
AWS_S3_FILE_OVERWRITE = config('loacl_aws_s3_file_overwrite')
AWS_S3_REGION_NAME = config('local_aws_s3_region_name') # Change to your region
AWS_S3_SIGNATURE_VERSION = config('local_aws_s3_signature_version')
#STATICFILES_STORAGE = storages.backends.s3boto3.S3Boto3Storage
