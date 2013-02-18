from django.test import TestCase
from django.db import IntegrityError

from nose import tools as nt

from domande.models import TextQuestion, ChoiceQuestion, Choice


class DomandeModelTests(TestCase):

    def test_questions(self):
        ''' Create a bunch of questions'''

        TextQuestion.objects.create(order=1,
            text='How much wood can a woodchuck chuck?')

        TextQuestion.objects.create(order=2,
            text='What is the meaning of life')

        questions = TextQuestion.objects.all()
        nt.eq_(questions.count(), 2)


class DemoCompQuestion(TestCase):

    def test_road_week8(self):
        ''' Test the db structure by using some sample data'''

        choice_label_text = [
            'Certified dolphin-safe',
            'Cooked to perfection',
            'High in quality protein',
            'Delicous',
            'Responsibly caught by the pole & line',
            'Greenpeace endorsed fishing-practices',
            'Natural source of omega-3s',
            'All of the above!'
        ]

        choices = [Choice.objects.create(order=i, label=label)\
                    for i, label in enumerate(choice_label_text)]

        question = ChoiceQuestion.objects.create(multichoice=True,
            text="Why do we love safcol tuna?")

        question.choices = choices
        choice = question.choices.filter(label__icontains='protein')
        nt.eq_(choice.count(), 1)
        nt.eq_(choice.all()[0].order, 2)


