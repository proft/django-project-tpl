# -*- coding: utf-8 -*-

# RUN: python manage.py test --settings={{ project_name }}.settings_test a

from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

SOUTH_TESTS_MIGRATE = False

