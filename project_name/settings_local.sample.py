from __future__ import absolute_import
"""
To use this, create a `.env` with DJANGO_SETTINGS_MODULE={{ project_name }}.settings_local
"""

from .settings import *

DEBUG = True

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SENTRY_DSN = None

INSTALLED_APPS.append(
    'debug_toolbar',
)

COMPRESS_MTIME_DELAY = 0
