from django.db import models
from django.contrib.contenttypes import generic

from domande.models import Question


class DummyModel(models.Model):
    ''' model used for testing '''

    name = models.CharField(max_length=256)
    questions = models.ManyToManyField(Question)

    def __unicode__(self):
        return self.name
