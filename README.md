![domande](https://raw.github.com/bulkan/django-domande/master/logo.png)

Logo by [@aurorachiarello](http://github.com/aurorachiarello)

[![Build Status](https://travis-ci.org/bulkan/django-domande.png?branch=master)](https://travis-ci.org/bulkan/django-domande)


A plugable django app to represent a questions.


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

```python
INSTALLED_APPS = [
   ...
   'crispy-forms'   # need to add this for it's template tags to load
   'domande'
   ...
]
```


__Note__ I'm assuming you have South already installed if not add ```south``` to ```INSTALLED_APPS```


Usage
=====

Create a model with a ManyToManyField to domande.models.Question. For example a Questionnaire;


```python
from django.db import models
from django.contrib.contenttypes import generic

from domande.models import Question, Answer

class Questionnaire(models.Model):
    name = models.CharField(max_length=256)

    questions = models.ManyToManyField(Question)
```


domande at the moment supports two question types. A TextQuestion in which the user answers is by entering text and a
a ChoiceQuestion, the answer being chosen by a set of choices.

Once you add a ManyToManyField to Question which is the base class that the two question types inherit from, the django 
admin interface will display the parent model with an additional step of choosing the which child model instance to create.


Now you need to render the list of Questions in a view;


```python
def questionnaire_view(request):

    # for sake of example use .get
    questionnaire = Questionnaire.objects.get(id=1)

    forms = [q.get_form()(prefix=str(q.id),
                content_object=request.user,
                question=q, form_tag=False)
                   for q in questionnaire.questions.all().get_real_instances()
               ]

    # form is a list of TextQuestionForm or ChoiceQuestionForm
```


domande's forms accept a ```content_object``` that it used when it saves an Answer.
As it doesn't know in advance what sort of "user" or "entry" model you have it uses
django's builtin ```ContentType``` framework to solve this. In the above example it uses
```request.user``` which is django's auth user


in the template render the forms like so;

```html
{% load crispy_forms_tags %}

<form method="post">
    {% for form in forms %}
        {% crispy form %}
    {% endfor %}
</form>
```

to process the validity of the forms and save the answers;

```python
forms = [q.get_form()(request.POST or None,
            prefix=str(q.id),
            content_object=request.user,
            question=q, form_tag=False)
                for q in survey.questions.all().get_real_instances()
        ]

forms_are_valid = []

for form in forms:
    forms_are_valid.append(valid)
    valid = form.is_valid()
    if valid:
        t = form.save()

forms_are_valid = all(forms_are_valid)
```

Development
-----------

Fork this repo, create a virtualenv and clone your fork. Then install the requirements

    pip install -r requirements.txt

If you have changed the models then create a migration;

    django-admin.py schemamigration --settings=domande.settings --pythonpath=$PWD

Please make sure existing tests pass and feel free to add more tests as you see fit.

    django-admin.py test --settings='tests.test_settings' --pythonpath=$PWD

Submit Pull Request
