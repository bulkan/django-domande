from django.forms import Form
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineRadios
from crispy_forms.layout import Layout

from models import TextQuestion


class QuestionForm(Form):
    ''' Base class for a Question
    '''

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        # TODO: get this from kwargs in the future
        #self.helper.form_class = 'form-horizontal'

        self.question = kwargs.get('question')

        if not self.question:
            raise ValueError('Need a question to render')

        del kwargs['question']
        super(QuestionForm, self).__init__(*args, **kwargs)

        # TODO: check for answers for content_object and use as
        # initial data


class TextQuestionForm(QuestionForm):
    def __init__(self, *args, **kwargs):
        super(TextQuestionForm, self).__init__(*args, **kwargs)

        self.fields['question'] = forms.CharField(
            label=self.question.text,
            widget=forms.TextInput(),
            required=not self.question.optional,
        )


class ChoiceQuestionForm(QuestionForm):
    def __init__(self, *args, **kwargs):
        super(ChoiceQuestionForm, self).__init__(*args, **kwargs)

        choices  = [(c.label, c.id) for c in self.question.choices.all()]

        field = forms.ChoiceField(
            label=self.question.text,
            required=not self.question.optional,
            choices=choices,
            widget=forms.RadioSelect()
        )

        self.fields['question'] = field

        # Render radio buttons inline
        self.helper.layout = Layout(
            InlineRadios('question')
        )
