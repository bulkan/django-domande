![domande](https://raw.github.com/bulkan/django-domande/master/logo.png)

Logo by [@aurorachiarello](http://github.com/aurorachiarello)

[![Build Status](https://travis-ci.org/bulkan/django-domande.png?branch=master)](https://travis-ci.org/bulkan/django-domande)



A plugable django app to represent a questions. Imagine a Survey. But


Dependencies
============

Here are the list of dependencies;

* [http://django-crispy-forms.readthedocs.org](django-crispy-forms) - This is used to render form fields with Bootstrap classes
* [https://github.com/chrisglass/django_polymorphic/](django_polymorphic) - Provides an easy way of doing model inheritence.
* [http://south.readthedocs.org/en/latest/](South) - For model migration. Please use it :smile:


Installation
===========

For stable PyPI version

    pip install django-domande


To get development version

    pip install git+git://github.com/bulkan/django-domande.git


In your ```settings.py``` file change ```INSTALLED_APPS``` and add;

   INSTALLED_APPS = [
    ...
    'crispy-forms'   # need to add this for it's template tags to load
    'domande'
    ...
   ]


Note I'm assuming you have South already installed if not add ```south``` to ```INSTALLED_APPS```



Development
-----------

Create a virtualenv and clone this repo. Then install the requirements

    pip install -r requirements.txt

If you have changed the models then create a migration;

    django-admin.py schemamigration --settings=domande.settings --pythonpath=$PWD

Please make sure existing tests pass. Add more tests as you see fit.

    django-admin.py test --settings='tests.test_settings' --pythonpath=$PWD

Submit Pull Request
