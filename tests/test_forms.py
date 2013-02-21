from django.template.loader import get_template_from_string
from django.forms import ValidationError

from django.template import Context, TemplateSyntaxError

from django.test import TestCase
from django.test.client import RequestFactory

from nose import tools as nt

from domande.forms import QuestionForm, TextQuestionForm, ChoiceQuestionForm
from domande.models import TextQuestion, ChoiceQuestion, Choice
from domande.models import TextAnswer, ChoiceAnswer

from .utils import BaseTest
from .models import DummyMember


request_factory = RequestFactory()


class TestForms(BaseTest):

    def test_no_question(self):
        '''Test that form raises ValueError when without a quesion
        being passed '''

        # This should raise a ValueError because of no question
        nt.assert_raises(ValueError, QuestionForm,
            content_object=self.member
        )

        # These should be ValueError's because of no content_type
        nt.assert_raises(ValueError, TextQuestionForm)
        nt.assert_raises(ValueError, ChoiceQuestionForm)


    def test_question_form(self):
        text_question = TextQuestion.objects.create(
            text='What is a text question?'
        )

        form =  TextQuestionForm(
            question=text_question,
            content_object=self.member
        )

        template = get_template_from_string(u"""
                {% load crispy_forms_tags %}
                {% crispy form %}
        """)

        form.is_valid()

        # can't save an invalid form
        nt.assert_raises(ValidationError, form.save)

        c = Context({'form': form})
        html = template.render(c)
        nt.assert_true('order' not in html)
        nt.assert_true('question' in html)


    def test_choice_question_form(self):
        choice_question = ChoiceQuestion.objects.create(
            text="What is the meaning of life?"
        )

        choice_question.choices = [
            Choice.objects.create(label='42 what was the question?'),
            Choice.objects.create(label='43'),
        ]

        form =  ChoiceQuestionForm(
            question=choice_question,
            content_object=self.member,
        )

        template = get_template_from_string(u"""
                {% load crispy_forms_tags %}
                {% crispy form %}
        """)
        nt.eq_(form.is_valid(), False)
        c = Context({'form': form})
        html = template.render(c)

        nt.assert_true('42 what was the question' in html)


    def test_choice_multichoice_question_form(self):
        choice_question = ChoiceQuestion.objects.create(
            text="Multichoice question",
            multichoice=True
        )

        choice_question.choices = [
            Choice.objects.create(label='42 what was the question?'),
            Choice.objects.create(label='43'),
        ]

        form = ChoiceQuestionForm(
            question=choice_question,
            content_object=self.member,
        )

        template = get_template_from_string(u"""
                {% load crispy_forms_tags %}
                {% crispy form %}
        """)
        nt.eq_(form.is_valid(), False)
        c = Context({'form': form})
        html = template.render(c)

        nt.assert_true('42 what was the question' in html)

        # test that inline checkboxes are rendering instead of radio buttons
        nt.assert_true('checkbox inline' in html)


    def test_textanswerform_save(self):
        ''' Test that TextAnswers are created via the form
        '''

        text_question = TextQuestion.objects.create(
            text='What is a text question?'
        )

        data = {'answer': 'testing'}

        form =  TextQuestionForm({},
            question=text_question,
            content_object=self.member
        )

        # question is required by default
        nt.assert_raises(ValidationError, form.save)

        form =  TextQuestionForm(data,
            question=text_question,
            content_object=self.member
        )

        # we shouldn't have any answers
        nt.eq_(TextAnswer.objects.all().count(), 0)

        # form is valid
        nt.eq_(form.is_valid(), True)

        # saving the form should create a new TextAnswer object
        form.save()
        nt.eq_(TextAnswer.objects.all().count(), 1)
        nt.eq_(TextAnswer.objects.all()[0].answer, data['answer'])


    def test_choiceanswerform_save(self):
        choice_question = ChoiceQuestion.objects.create(
            text="Multichoice question",
            multichoice=True
        )

        choice_question.choices = [
            Choice.objects.create(label='42 what was the question?'),
            Choice.objects.create(label='43'),
        ]

        data = {'answer': [1]}

        form = ChoiceQuestionForm({},
            question=choice_question,
            content_object=self.member,
        )

        # question is required by default
        nt.assert_raises(ValidationError, form.save)


        form = ChoiceQuestionForm(data,
            question=choice_question,
            content_object=self.member,
        )

        # form should be  valid now
        nt.eq_(form.is_valid(), True)

        # we shouldn't have any answers
        nt.eq_(ChoiceAnswer.objects.all().count(), 0)

        # form is valid
        nt.eq_(form.is_valid(), True)

        # saving the form should create a new TextAnswer object
        form.save()
        nt.eq_(ChoiceAnswer.objects.all().count(), 1)
        saved_answer_choices = set(ChoiceAnswer.objects.all()[0]\
            .answer.all().values_list('id', flat=True))
        nt.eq_(saved_answer_choices, set(data['answer']))

        form.save()
