from django.test import TestCase
from domande.models import TextQuestion


class DomandeModelTests(TestCase):

    def test_questions(self):
        ''' Create a bunch of questions'''

        TextQuestion.objects.create(order=1,
            text='How much wood can a woodchuck chuck?')
