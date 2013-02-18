#import os


#FOLDER_ROOT = os.path.normpath(os.path.dirname(__file__))

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

INSTALLED_APPS = [
    'domande',
    'django_extensions',
    'south',
]

SOUTH_TESTS_MIGRATE = False
