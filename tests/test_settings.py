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
    'django_nose'
]

SOUTH_TESTS_MIGRATE = False

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
