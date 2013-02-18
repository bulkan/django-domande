![domande](https://raw.github.com/bulkan/django-domande/master/logo.png)(http://aurorachiarello.com)

[![Build Status](https://travis-ci.org/bulkan/django-domande.png?branch=master)](https://travis-ci.org/bulkan/django-domande)


django-domande
==============

django app to create multiple questions


Development
-----------

Creating migrations;

    django-admin.py schemamigration --settings=domande.settings --pythonpath=$PWD

* Make sure that settings file contains entries for DATABASES and INSTALLED_APPS contains ```domande``` and ```South```

Notes
=====

Can't use Django ORM aggregation when you use a GenericForeignKey and a GenericRelation

User should create a ManyToManyField on their model that needs questions


