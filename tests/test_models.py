from django.db import models
from django.db import IntegrityError

from django.contrib.contenttypes.models import ContentType

from django.test import TestCase

from nose import tools as nt

from domande.models import TextQuestion, ChoiceQuestion, Choice
from domande.models import TextAnswer, ChoiceAnswer
from domande.models import Question

from models import DummyModel, DummyMember


class DomandeModelTests(TestCase):

    def test_text_questions(self):
        '''Create a bunch of text questions'''

        dummy = DummyModel.objects.create(name='dumb dumb')

        question_texts = [
            'How much wood can a woodchuck chuck?',
            'What is the meaning of life'
        ]

        for i, text in enumerate(question_texts):
            t = TextQuestion.objects.create(order=i,
                text=text)
            dummy.questions.add(t)

        sorted([question.text for question in dummy.questions.all()])

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

        dummy = DummyModel.objects.create(name="dumber")

        choices = [Choice.objects.create(order=i, label=label)\
                    for i, label in enumerate(choice_label_text)]

        choice_question = ChoiceQuestion.objects.create(multichoice=True,
            text="Why do we love safcol tuna?")

        dummy.questions.add(choice_question)

        choice_question.choices = choices
        choice = choice_question.choices.filter(label__icontains='protein')
        nt.eq_(choice.count(), 1)
        nt.eq_(choice.all()[0].order, 2)

        text_question = TextQuestion.objects.create(order=1,
            text='How much wood can a woodchuck chuck?')

        dummy.questions.add(text_question)

        # we created two questions so we should get 2 back
        nt.eq_(dummy.questions.all().count(), 2)


class TestAnswerModels(TestCase):

    def setUp(self):
        # create a dummy member
        self.member = DummyMember.objects.create(name="Tester")

        self.member2 = DummyMember.objects.create(name='Another member')
        self.ctype = ContentType.objects.get_for_model(self.member)

    def test_text_answer(self):
        '''
        Test that the reverse GenericRelation works
        '''

        text_question = TextQuestion.objects.create(order=1,
            text='How much wood can a woodchuck chuck?')

        for i in range(2):
            # answer belongs to member
            answer = TextAnswer.objects.create(
                question=text_question,
                answer="4%d woods" %i,
                content_object=self.member,
            )

        nt.eq_(self.member.answers.count(), 2)

        # Test that we can get the answer object
        nt.eq_(self.member.answers.all()[1], answer)

        # Test the we can get the question from answer
        nt.eq_(self.member.answers.all()[1].question, text_question)


    def test_choice_answer(self):
        '''
        Test Choice answers
        '''

        choices = [Choice.objects.create(label=t) for t in ('42', '43', '45')]

        choice_question = ChoiceQuestion.objects.create(
            text='What is the meaning of life?'
        )

        choice_question.choices = choices

        choice_answer = ChoiceAnswer.objects.create(
            question=choice_question,
            content_object=self.member,
        )

        choice_answer.answer = choices[:2]

        # Test that we can get the answer object
        nt.eq_(self.member.answers.count(), 1)

        # Test that we can find same Choices that was 'selected'
        nt.eq_(set(choices[:2]), set(self.member.answers.all()[0].answer.all()))

        # The second member shouldnt have any answers
        nt.eq_(self.member2.answers.count(), 0)
