from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


from polymorphic import PolymorphicModel

from django_extensions.db.models import TimeStampedModel



class Question(PolymorphicModel, TimeStampedModel):
    '''
        Represents a question.
    '''

    class Meta:
        ordering = ['order']

    order = models.PositiveIntegerField(default=1,
        help_text='The render order')

    optional = models.BooleanField(default=False,
            help_text="If selected, user doesn't have to answer this question")

    text = models.TextField(blank=False,
        help_text='The question text')

    def __unicode__(self):
        return self.text


class TextQuestion(Question):
    '''
    Question with a text answer
    '''

    def get_form(self):
        '''
        Returns the form for this model
        '''
        from forms import TextQuestionForm
        return TextQuestionForm


class Choice(TimeStampedModel):
    '''
    Model to store the choices for multi choice questions
    '''

    order = models.PositiveIntegerField(default=1)

    label = models.TextField(default="")

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.label


class ChoiceQuestion(Question):
    '''
    Question with answers that are chosen from a list of choices defined
    by the user.
    '''

    multichoice = models.BooleanField(default=False,
            help_text="Select one or more")

    choices = models.ManyToManyField(Choice)

    def get_form(self):
        '''
        Returns the form for this model
        '''

        from forms import ChoiceQuestionForm
        return ChoiceQuestionForm


class Answer(PolymorphicModel, TimeStampedModel):
    ''' Base Answer model
    '''
    question = models.ForeignKey(Question)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')


class TextAnswer(Answer):
    answer = models.TextField(blank=False,
        help_text = 'The answer text')

    def __unicode__(self):
        return self.answer


class ChoiceAnswer(Answer):
    answer = models.ManyToManyField(Choice,
        help_text='The selected choices as the answer')

    def __unicode__(self):
        return self.question

        # XXX: the following does a weird recursion depth exception o_O ?
        #''.join(self.answer.all().values_list('label', flat=True))
