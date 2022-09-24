from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
# from django.template import loader

from .models import Question


# polls/index.html 템플릿을 불러와 context를 전달
# context는 템플릿에서 쓰이는 변수명과 Python 객체를 연결
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

    # legacy code (using template without render)
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

    # legacy code (basic 404 error handler)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
