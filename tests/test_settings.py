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
    'django.contrib.contenttypes',
    'django_extensions',
    'crispy_forms',
    'south',
    'tests', # need to add this so my dummy models are created
    'domande',
    'django_nose',
]

SOUTH_TESTS_MIGRATE = False

NOSE_ARGS = ['-s',
             '--with-cover',
             #'--with-xunit',
             '--cover-package=domande',
             '--cover-html',
]

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

ROOT_URLCONF = 'tests.urls'

SECRET_KEY = 'not so secret key'
