# Django settings for {{ project_name }} project.
import os
import sys
import re

# DEBUG based settings.
DEBUG = os.environ.get('DJANGO_DEBUG', 'True').lower() in ('t', 'true', 'y', 'yes', '1')

# For debugging sorl thumbnailer
#THUMBNAIL_DEBUG = True

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

ADMINS = (
    ('Programmers', 'programmers@fusionbox.com'),
)

MANAGERS = ADMINS

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {'default': dj_database_url.config(default='sqlite:///sqlite_database')}
DATABASES['default']['ATOMIC_REQUESTS'] = True

TIME_ZONE = 'America/Denver'
SITE_ID = 1
USE_L10N = True
USE_TZ = True
LANGUAGES = []
# Set Sorl Thumbnailer to png to preserve transparent backgrounds
THUMBNAIL_FORMAT = 'PNG'

# Set the site title in Grappelli
GRAPPELLI_ADMIN_TITLE = '{{ project_name }} Admin Center'

MEDIA_ROOT = os.path.join(PROJECT_PATH, '..', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_PATH, '..', "static")
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'public'),
)

STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Production installs need to have this environment variable set
DEFAULT_SECRET_KEY = '{{ secret_key }}'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', DEFAULT_SECRET_KEY)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_PATH, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'fusionbox.middleware.GenericTemplateFinderMiddleware',
    'fusionbox.middleware.RedirectFallbackMiddleware',
)

# This prevents clickjacking <http://en.wikipedia.org/wiki/Clickjacking>
X_FRAME_OPTIONS = 'SAMEORIGIN'

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'
FORCE_SCRIPT_NAME = ''

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',  # Must go before admin.
    'django.contrib.admin',

    # 3rd party
    'compressor',
    'cachebuster',
    'fusionbox.core',
    'django_extensions',
    'raven.contrib.django',
    'bandit',
    'test_pep8',
    'backupdb',
    'authtools',

    # Project
    '{{ project_name }}',
]

# test_pep8 config
TEST_PEP8_DIRS = (
    os.path.dirname(PROJECT_PATH),
)
TEST_PEP8_EXCLUDE = (
    'migrations',
)
TEST_PEP8_IGNORE = (
    'E501',  # Line length of 80 chars
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'DEBUG',
        'handlers': ['sentry', 'console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'exception': {
            'level': 'ERROR',
            'class': '{{ project_name }}.exception_logging.ExceptionHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'sentry'],
            'level': 'DEBUG',
        },
        'werkzeug': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'scss': {
            'level': 'ERROR',
            'handlers': ['exception'],
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

# django-compressor setting
COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_pyscss.compressor.DjangoScssFilter'),
)

# authtools
AUTH_USER_MODEL = 'authtools.User'


SESSION_COOKIE_HTTPONLY = True

INTERNAL_IPS = (
    '127.0.0.1',
    '208.186.116.206',
    '208.186.142.130',
)

# For `send_markdown_email` and emailtools email sending.
EMAIL_LAYOUT = 'mail/base.html'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


IGNORABLE_404_URLS = (
    re.compile(r'\.(php|cgi)$'),
    re.compile(r'/null/?$'),
    re.compile(r'^/phpmyadmin/', re.IGNORECASE),
    re.compile(r'^/favicon\.ico.*$'),
    re.compile(r'^/wp-admin/'),
    re.compile(r'^/cgi-bin/'),
    re.compile(r'^(?!/static/).*\.(css|js)/?$'),
)

DATABASE_ENGINE = DATABASES['default']['ENGINE']

# Attempt to configure sentry from an environment variable.
try:
    SENTRY_DSN = os.environ['SENTRY_DSN']
except KeyError:
    pass
