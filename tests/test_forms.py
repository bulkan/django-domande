from django.template.loader import get_template_from_string

from django.template import Context, TemplateSyntaxError

from django.test import TestCase
from django.test.client import RequestFactory

from nose import tools as nt

from domande.forms import QuestionForm, TextQuestionForm, ChoiceQuestionForm


request_factory = RequestFactory()


def test_question_form():
    form =  TextQuestionForm()

    template = get_template_from_string(u"""
            {% load crispy_forms_tags %}
            {{ form|crispy}}
    """)

    form.is_valid()

    c = Context({'form': form})
    html = template.render(c)
    nt.eq_('order' not in html, True)


def test_answer():
    request = request_factory.post(
        path = '/',
        data = {
         'answer': 'testing'
        }
    )
