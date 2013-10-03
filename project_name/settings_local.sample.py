"""
To use this, create a `.env` with DJANGO_SETTINGS_MODULE={{ project_name }}.settings_local
"""
from settings_base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SENTRY_DSN = None
