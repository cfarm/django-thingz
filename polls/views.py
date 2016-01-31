
from .models import Question
from django.shortcuts import render

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    pulled_question = Question.objects.get(id=question_id)
    context = {'pulled_question': pulled_question}
    return render(request, 'polls/detail.html', context)    

def results(request, question_id):
    context = {'question_id': question_id}
    return render(request, 'polls/results.html', context)

def vote(request, question_id):
    context = {'question_id': question_id}
    return render(request, 'polls/vote.html', context)
    # return HttpResponse("You're voting on question %s." % question_id)
