from django.db import models

from django_extensions.db.models import TimeStampedModel


class BaseQuestion(TimeStampedModel):
    ''' represents a question '''

    class Meta:
        abstract = True
        ordering = ['order']

    order = models.PositiveIntegerField(default=1,
        help_text='The render order')

    optional = models.BooleanField(default=False,
            help_text="If selected, user doesn't have to answer this question")

    text = models.TextField(blank=False,
        help_text='The question text')

    def __unicode__(self):
        return self.text


class TextQuestion(BaseQuestion):
    pass


class Choice(TimeStampedModel):
    ''' Model to store the choices for multi answer questions'''

    order = models.PositiveIntegerField(default=1)

    label = models.TextField(default="")

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.label


class ChoiceQuestion(BaseQuestion):
    multichoice = models.BooleanField(default=False,
            help_text="Select one or more")

    choices = models.ManyToManyField(Choice)


class BaseAnswer(TimeStampedModel):
    class Meta:
        abstract = True


class TextAnswer(BaseAnswer):
    question =  models.ForeignKey(TextQuestion)

    answer = models.TextField(blank=False,
        help_text = 'The answer text')

    def __unicode__(self):
        return self.question


class ChoiceAnswer(BaseAnswer):
    question =  models.ForeignKey(TextQuestion)

    answer = models.ManyToManyField(Choice,
        help_text='The selected choices as the answer')

    def __unicode__(self):
        return self.answer

