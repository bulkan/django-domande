DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}


INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django_extensions',
    'south',
    'domande'
]


SECRET_KEY = 'lol im secret'
