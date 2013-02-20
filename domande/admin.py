from django.contrib import admin
from models import Question, TextQuestion, ChoiceQuestion, Choice

admin.site.register(Question)
admin.site.register(TextQuestion)
admin.site.register(ChoiceQuestion)
admin.site.register(Choice)
