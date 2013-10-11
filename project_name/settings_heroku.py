"""
Working on heroku requires the following environment variables to be present.

# Amazon AWS config
AWS_ACCESS_KEY_ID - the access id for aws
AWS_SECRET_ACCESS_KEY - the secret key for aws
AWS_STORAGE_BUCKET_NAME - the name of the s3 bucket.

# Django config
DJANGO_SECRET_KEY - the secret key for the project
DJANGO_SETTINGS_MODULE - the location of the settings module heroku should use ({{ project_name }}.settings_heroku)

# Email config
EMAIL_HOST
EMAIL_PORT
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
"""
from .settings_base import *  # NOQA
from .settings_aws import *  # NOQA

if 'DJANGO_DEBUG' in os.environ:
    DEBUG = (os.environ['DJANGO_DEBUG'] == 'True')
else:
    DEBUG = False

# setup connection pooling
DATABASES['default']['ENGINE'] = 'django_postgrespool'

SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.postgresql_psycopg2'
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = [
    '{{ project_name }}.dev.fusionbox.com',
    '{{ project_name }}.herokuapp.com',
]

# Django Compressor
COMPRESS_ENABLED = True
COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_STORAGE = STATICFILES_STORAGE

if DEBUG is False:
    # Sanity check to be sure that we aren't running production without a
    # secure secret key.
    assert not SECRET_KEY == 'not-really-a-very-good-secret-key-now-is-it-so-set-a-better-one'

# Email configuration
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = True

# Hijack outbound email and send it all to `BANDIT_EMAIL`
if DEBUG is True:
    EMAIL_BACKEND = 'bandit.backends.smtp.HijackSMTPBackend'
    BANDIT_EMAIL = os.environ.get('BANDIT_EMAIL', 'paula@fusionbox.com')

from memcacheify import memcacheify

CACHES = memcacheify()

if not DEBUG:
    # if not `running in runserver` would be a better condition here
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
    )

# In a non-DEBUG environment, don't allow the app to start without a
# `SENTRY_DSN` value
try:
    assert bool(SENTRY_DSN)
except (NameError, AssertionError):
    if DEBUG:
        import warnings
        warnings.warn('Missing Sentry DSN Value.  Error reporting will not be reported to sentry')
    else:
        from django.core.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured('DSN Value Missing.  Error reporting will not be reported to sentry')
