from django.contrib import admin

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from models import Question, TextQuestion, ChoiceQuestion, Choice
from models import Answer, TextAnswer, ChoiceAnswer


class QuestionChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Question

    # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
    # the additional fields of the child models are automatically added to the admin form.
    #base_form = ...
    #base_fieldsets = (
        #...
    #)


class TextQuestionAdmin(QuestionChildAdmin):
    base_model = TextQuestion


class ChoiceQuestionAdmin(QuestionChildAdmin):
    """ Base admin class for all child models """
    #base_model = ChoiceQuestion


class QuestionParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = Question
    child_models = (
        (TextQuestion, TextQuestionAdmin),
        (ChoiceQuestion, ChoiceQuestionAdmin),
    )



admin.site.register(Question, QuestionParentAdmin)
#admin.site.register(TextQuestion)
admin.site.register(TextAnswer)
#admin.site.register(ChoiceQuestion)
admin.site.register(ChoiceAnswer)
admin.site.register(Choice)
