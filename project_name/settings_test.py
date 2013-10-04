DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'test_database',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Dev DSN Value
SENTRY_DSN = ''

# Tell raven to report errors even when debug is True
RAVEN_CONFIG = {
    'register_signals': False,
}
