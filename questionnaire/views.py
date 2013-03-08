from .models import Questionnaire


def questionnaire_view(request):

    # for sake of example use .get
    questionnaire = Questionnaire.objects.get(id=1)

    forms = [q.get_form()(prefix=str(q.id),
                content_object=request.user,
                question=q, form_tag=False)
                   for q in questionnaire.questions.all().get_real_instances()
               ]

    # form is a list of TextQuestionForm or ChoiceQuestionForm
