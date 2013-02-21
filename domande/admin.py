from django.contrib import admin
from models import Question, TextQuestion, ChoiceQuestion, Choice
from models import Answer, TextAnswer, ChoiceAnswer

admin.site.register(Question)
admin.site.register(TextQuestion)
admin.site.register(TextAnswer)
admin.site.register(ChoiceQuestion)
admin.site.register(ChoiceAnswer)
admin.site.register(Choice)
