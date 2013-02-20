from django.template.loader import get_template_from_string

from django.template import Context, TemplateSyntaxError

from django.test import TestCase
from django.test.client import RequestFactory

from nose import tools as nt

from domande.forms import QuestionForm, TextQuestionForm, ChoiceQuestionForm
from domande.models import TextQuestion

from .models import DummyMember


request_factory = RequestFactory()


class TestForms(TestCase):

    def setUp(self):
        # create a dummy member
        self.member = DummyMember.objects.create(name="Tester")

        self.text_question = TextQuestion.objects.create(order=1,
            text='How much wood can a woodchuck chuck?')


    def test_no_question(self):
        '''Test that form raises ValueError when without a quesion
        being passed '''

        nt.assert_raises(ValueError, QuestionForm)
        nt.assert_raises(ValueError, TextQuestionForm)
        nt.assert_raises(ValueError, ChoiceQuestionForm)


    def test_question_form(self):
        form =  TextQuestionForm(question=self.text_question)

        template = get_template_from_string(u"""
                {% load crispy_forms_tags %}
                {{ form|crispy}}
        """)

        form.is_valid()

        c = Context({'form': form})
        html = template.render(c)
        nt.eq_('order' not in html, True)
        nt.eq_('question' in html, True)


def test_answer():
    request = request_factory.post(
        path = '/',
        data = {
         'answer': 'testing'
        }
    )
