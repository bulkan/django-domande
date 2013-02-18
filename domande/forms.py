from django.forms import ModelForm

from crispy_forms.helper import FormHelper

from models import TextQuestion


class TextQuestionForm(ModelForm):
    class Meta:
        model = TextQuestion
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        super(TextQuestionForm, self).__init__(*args, **kwargs)
