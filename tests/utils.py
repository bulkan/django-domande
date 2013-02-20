from django.contrib.contenttypes.models import ContentType

from django.test import TestCase

from domande.forms import QuestionForm, TextQuestionForm, ChoiceQuestionForm
from domande.models import TextQuestion, ChoiceQuestion, Choice

from .models import DummyMember, DummyModel


class BaseTest(TestCase):
    ''' BaseTest case that all should inherit from
    '''

    def setUp(self):
        # create a dummy member
        self.member = DummyMember.objects.create(name="Tester")

        self.member2 = DummyMember.objects.create(name='Another member')
        self.ctype = ContentType.objects.get_for_model(self.member)

        self.dummy = DummyModel.objects.create(name='dumb dumb')
