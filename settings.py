import environ
import dj_database_url
import os
from keys import SECRET_KEY, PAYMENT_METHOD_SECRET 

env = environ.Env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = env.bool('DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'silver',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'silver.urls'
WSGI_APPLICATION = 'silver.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        env='DATABASE_URL',
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')
    )
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}

#CELERY_BROKER_URL = env('REDIS_URL', default='redis://redis:6379/0')
#CELERY_RESULT_BACKEND = env('REDIS_URL', default='redis://redis:6379/0')
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_BROKER_TRANSPORT = 'redis'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

PAYMENT_PROCESSORS = {
    'manual': {
        'class': 'silver.payment_processors.ManualProcessor',
        'name': 'Manual Payment Processor',
    },
}

LOCK_MANAGER_CONNECTION = {
#    'host': env('REDIS_HOST', default='redis'),
    'host': 'redis',
    'port': 6379,
    'db': 1,
}

PAYMENT_METHOD_SECRET = 'pSZUL6cYaH6-E_OA-mlRuURgGHmn0wd5J7HwRk60A2s='

# Silver payment processors configuration
PAYMENT_PROCESSORS = {
    'manual': {
        'class': 'silver.payment_processors.ManualProcessor',
        'name': 'Manual Payment Processor',
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'xhtml2pdf': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'pisa': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'pycountry.db': {
            'handlers': ['console'],
            'level': 'ERROR',  # Suppress DEBUG warnings
            'propagate': False,
        },
    },
}
