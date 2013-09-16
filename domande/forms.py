from django import forms

from django.db.models import Count
from django.contrib.contenttypes.models import ContentType

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineRadios, InlineCheckboxes
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit


from models import TextAnswer, ChoiceAnswer, Choice

# List of validator_name:func_name
# Show in admin a multichoice list of validator names
# pass this to form using field_name='validator_name' ?


class QuestionForm(forms.Form):
    ''' Base class for a Question
    '''

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        # If true crispy-forms will render a <form>..</form> tags
        self.helper.form_tag = kwargs.get('form_tag', True)

        if 'form_tag' in kwargs:
            del kwargs['form_tag']

        self.content_object = kwargs.get('content_object')
        if not self.content_object:
            raise ValueError('Need a content_object to save answers too')

        self.content_type = ContentType.objects.get_for_model(self.content_object)

        del kwargs['content_object']

        self.helper.form_class = kwargs.get('form_class', '')

        self.question = kwargs.get('question')

        if not self.question:
            raise ValueError('Need a question to render')

        del kwargs['question']
        super(QuestionForm, self).__init__(*args, **kwargs)




class TextQuestionForm(QuestionForm):
    def __init__(self, *args, **kwargs):
        super(TextQuestionForm, self).__init__(*args, **kwargs)

        # work out initial data

        initial_answer = TextAnswer.objects.filter(
            object_id=self.content_object.id,
            question=self.question
        )

        initial_answer = initial_answer[0].answer if initial_answer.exists() else ''

        self.fields['answer'] = forms.CharField(
            label=self.question.text,
            widget=forms.TextInput(),
            required=not self.question.optional,
            initial=initial_answer,
        )
        answer = self.fields['answer']

    def save(self):
        if not self.is_valid():
            raise forms.ValidationError('form is not valid')

        answer = self.cleaned_data.get('answer')

        if not answer:
            if self.fields['answer'].required:
                raise forms.ValidationError, 'Required'
            return

        text_answer, created = TextAnswer.objects.get_or_create(
            object_id=self.content_object.id,
            content_type=self.content_type,
            question=self.question,
            answer=answer
        )

        if created:
            text_answer.content_object = self.content_object
            text_answer.save()


class ChoiceQuestionForm(QuestionForm):
    def __init__(self, *args, **kwargs):
        super(ChoiceQuestionForm, self).__init__(*args, **kwargs)

        choices = [(c.id, c.label) for c in self.question.choices.all()]

        # initial values

        initial_choices = []
        choice_answer = ChoiceAnswer.objects.filter(
            object_id=self.content_object.id,
            question=self.question,
        ).annotate(a=Count('answer')).filter(a__gt=0)

        # we have ChoiceAnswer instance
        if choice_answer:
            choice_answer = choice_answer[0]
            initial_choices = choice_answer.answer.all().values_list('id', flat=True)
            if self.question.multichoice is False:
                initial_choices = initial_choices=[0]


        # default classes
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
            initial=initial_choices,
            widget=widget
        )

        self.fields['answer'] = field

        # Render choice buttons inline
        self.helper.layout = Layout(
            inline_type('answer')
        )

    def clean_answer(self):
      real_answer = self.cleaned_data.get('answer')

      # for single choice questions, the selected answer is a single string
      if type(real_answer) is not list:
        real_answer = [real_answer]
      return real_answer


    def save(self):
        if not self.is_valid():
            raise forms.ValidationError('Form is not valid')

        real_answer = self.cleaned_data.get('answer')

        if not real_answer:
            if self.fields['answer'].required:
                raise forms.ValidationError, 'Required'
            return

        choices = Choice.objects.filter(id__in=real_answer)

        # find ChoiceAnswer and filter in answer !
        choice_answer = ChoiceAnswer.objects.filter(
            object_id=self.content_object.id,
            content_type=self.content_type,
            question=self.question,
        )

        # we have ChoiceAnswer instance
        if choice_answer:
            choice_answer = choice_answer[0]

        if not choice_answer:
            # create a ChoiceAnswer
            choice_answer  = ChoiceAnswer.objects.create(
                object_id=self.content_object.id,
                content_type=self.content_type,
                question=self.question
            )

        # re save out the choices
        choice_answer.content_object = self.content_object
        choice_answer.answer = choices
        choice_answer.save()
