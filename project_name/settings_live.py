from __future__ import absolute_import

import os
import dj_database_url

from .settings import *

DEBUG = False

DATABASES = {'default': dj_database_url.config()}
DATABASES['default']['ATOMIC_REQUESTS'] = True

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
TEMPLATES[0]['OPTIONS']['loaders'] = (
    ('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders']),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': '{{ project_name }}-live',
    }
}

ALLOWED_HOSTS = ['www.{{ project_name }}.com']

BACKUPDB_DIRECTORY = os.environ['BACKUP_DIR']
MEDIA_ROOT = os.environ['MEDIA_ROOT']
STATIC_ROOT = os.environ['STATIC_ROOT']


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_PORT = 465
EMAIL_HOST_USER = 'webserver@{{ project_name }}.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
