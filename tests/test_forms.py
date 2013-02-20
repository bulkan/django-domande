from django.template.loader import get_template_from_string

from django.template import Context, TemplateSyntaxError

from django.test import TestCase
from django.test.client import RequestFactory

from nose import tools as nt

from domande.forms import QuestionForm, TextQuestionForm, ChoiceQuestionForm
from domande.models import TextQuestion, ChoiceQuestion, Choice

from .utils import BaseTest
from .models import DummyMember


request_factory = RequestFactory()


class TestForms(BaseTest):

    def test_no_question(self):
        '''Test that form raises ValueError when without a quesion
        being passed '''

        nt.assert_raises(ValueError, QuestionForm)
        nt.assert_raises(ValueError, TextQuestionForm)
        nt.assert_raises(ValueError, ChoiceQuestionForm)


    def test_question_form(self):
        text_question = TextQuestion.objects.create(
            text='What is a text question?'
        )

        form =  TextQuestionForm(question=text_question)

        template = get_template_from_string(u"""
                {% load crispy_forms_tags %}
                {% crispy form %}
        """)

        form.is_valid()

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

        form =  ChoiceQuestionForm(question=choice_question)

        template = get_template_from_string(u"""
                {% load crispy_forms_tags %}
                {% crispy form %}
        """)
        form.is_valid()
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

        form = ChoiceQuestionForm(question=choice_question)

        template = get_template_from_string(u"""
                {% load crispy_forms_tags %}
                {% crispy form %}
        """)
        form.is_valid()
        c = Context({'form': form})
        html = template.render(c)

        nt.assert_true('42 what was the question' in html)

        # test that inline checkboxes are rendering instead of radio buttons
        nt.assert_true('checkbox inline' in html)


    def test_answer(self):
        request = request_factory.post(
            path = '/',
            data = {
             'answer': 'testing'
            }
        )
