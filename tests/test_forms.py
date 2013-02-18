from django.template.loader import get_template_from_string

from django.template import Context, TemplateSyntaxError

from django.test import TestCase
from nose import tools as nt

from domande.forms import TextQuestionForm


def test_question_form():
    form =  TextQuestionForm()

    template = get_template_from_string(u"""
            {% load crispy_forms_tags %}
            {{ form|crispy}}
    """)

    form.is_valid()

    c = Context({'form': form})
    html = template.render(c)
    print html



