from django.forms import Form
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineRadios, InlineCheckboxes
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

        choices = [(c.id, c.label) for c in self.question.choices.all()]

        widget = forms.RadioSelect
        field_type = forms.ChoiceField
        inline_type = InlineRadios

        if self.question.multichoice:
            field_type = forms.MultipleChoiceField
            widget = forms.CheckboxSelectMultiple
            inline_type = InlineCheckboxes

        field = field_type(
            label=self.question.text,
            required=not self.question.optional,
            choices=choices,
            widget=widget
        )

        self.fields['question'] = field

        # Render radio buttons inline
        self.helper.layout = Layout(
            inline_type('question')
        )
