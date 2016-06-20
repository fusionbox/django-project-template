from __future__ import absolute_import

from .settings import *

DEBUG = True
THUMBNAIL_DEBUG = True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# Hijack all emails and send them to the BANDIT_EMAIL address
EMAIL_BACKEND = 'bandit.backends.smtp.HijackSMTPBackend'
BANDIT_EMAIL = 'bandit@fusionbox.com'

# Tell raven to report errors even when debug is True
RAVEN_CONFIG = {
    'register_signals': True,
}

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': '{{ project_name }}',
    }
}

BACKUPDB_DIRECTORY = os.environ['BACKUP_DIR']
MEDIA_ROOT = os.environ['MEDIA_ROOT']
STATIC_ROOT = os.environ['STATIC_ROOT']
