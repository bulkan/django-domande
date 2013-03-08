from django.db import models

from django.db import models
from django.contrib.contenttypes import generic

from domande.models import Question, Answer


class Questionnaire(models.Model):
    '''
    The model that needs to thats needs to ask questions.
    '''

    name = models.CharField(max_length=256)

    questions = models.ManyToManyField(Question)
