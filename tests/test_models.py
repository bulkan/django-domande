from django.db import models
from django.db import IntegrityError

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from django.test import TestCase


from nose import tools as nt

from domande.models import TextQuestion, ChoiceQuestion, Choice
from domande.models import Question

from models import DummyModel


class DomandeModelTests(TestCase):

    def test_text_questions(self):
        ''' Create a bunch of text questions'''

        dummy = DummyModel.objects.create(name='dumb dumb')

        question_texts = [
            'How much wood can a woodchuck chuck?',
            'What is the meaning of life'
        ]

        tgt = ContentType.objects.get_for_model(TextQuestion)

        for i, text in enumerate(question_texts):
            t = TextQuestion.objects.create(order=i,
                text=text)

            # Create Question objects of with the content_type of
            # TextQuestion
            q = Question.objects.create(content_type=tgt, object_id=t.id)
            dummy.questions.add(q)

        sorted([question.content_object.text for question in dummy.questions.all()])

        questions = dummy.questions.all()
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

        dummy = DummyModel(name="dumber")
        dummy.save()

        choices = [Choice.objects.create(order=i, label=label)\
                    for i, label in enumerate(choice_label_text)]

        choice_question = ChoiceQuestion.objects.create(multichoice=True,
            text="Why do we love safcol tuna?")

        ctype = ContentType.objects.get_for_model(ChoiceQuestion)

        q = Question.objects.create(content_type=ctype,
            object_id=choice_question.id)
        dummy.questions.add(q)

        choice_question.choices = choices
        choice = choice_question.choices.filter(label__icontains='protein')
        nt.eq_(choice.count(), 1)
        nt.eq_(choice.all()[0].order, 2)

        text_question = TextQuestion.objects.create(order=1,
            text='How much wood can a woodchuck chuck?')

        ctype = ContentType.objects.get_for_model(TextQuestion)
        q = Question.objects.create(content_type=ctype,
            object_id=text_question.id)
        dummy.questions.add(q)

        nt.eq_(dummy.questions.all().count(), 2)
