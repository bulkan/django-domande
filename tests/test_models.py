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

    def test_questions(self):
        ''' Create a bunch of questions'''


        dummy = DummyModel(name='dumb dumb')
        dummy.save()
        dummy_model_type = ContentType.objects.get_for_model(dummy)

        t = TextQuestion.objects.create(order=1,
            text='How much wood can a woodchuck chuck?')
        t.save()

        Question.objects.create(content_object=dummy,
            object_id=t.pk).save()

        t = TextQuestion.objects.create(order=2,
            text='What is the meaning of life')
        t.save()

        Question.objects.create(content_object=dummy,
            object_id=t.pk).save()

        questions = dummy.questions.all()
        print questions
        nt.eq_(questions.count(), 2)

        #ctype = ContentType.objects.get_for_model(DummyModel)
        #nt.eq_(TextQuestion.objects.filter(content_type=ctype).count(), 2)


#class DemoCompQuestion(TestCase):

    #def test_road_week8(self):
        #''' Test the db structure by using some sample data'''

        #choice_label_text = [
            #'Certified dolphin-safe',
            #'Cooked to perfection',
            #'High in quality protein',
            #'Delicous',
            #'Responsibly caught by the pole & line',
            #'Greenpeace endorsed fishing-practices',
            #'Natural source of omega-3s',
            #'All of the above!'
        #]

        #dummy = DummyModel(name="dumber")
        #dummy.save()

        #choices = [Choice.objects.create(order=i, label=label)\
                    #for i, label in enumerate(choice_label_text)]

        #question = ChoiceQuestion.objects.create(multichoice=True,
            #text="Why do we love safcol tuna?", 
            #content_object=dummy)

        #question.choices = choices
        #choice = question.choices.filter(label__icontains='protein')
        #nt.eq_(choice.count(), 1)
        #nt.eq_(choice.all()[0].order, 2)

        #TextQuestion.objects.create(order=1, content_object=dummy,
            #text='How much wood can a woodchuck chuck?')

        #ctype = ContentType.objects.get_for_model(DummyModel)
        #nt.eq_(TextQuestion.objects.filter(content_type=ctype).count(), 1)
