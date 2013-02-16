[![Build Status](https://travis-ci.org/bulkan/django-domande.png?branch=master)](https://travis-ci.org/bulkan/django-domande)

django-domande
==============

django app to create multiple questions


Development
-----------

Creating migrations;

    django-admin.py schemamigration --settings=domande.settings --pythonpath=$PWD

* Make sure that settings file contains entries for DATABASES and INSTALLED_APPS contains ```domande``` and ```South```
