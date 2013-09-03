from base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS += (
    #'debug_toolbar',
    'django_extensions',
)

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES += (
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
}

