
from django.shortcuts import render
from core.models import Question, Answer, Star
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import AddQuestion
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User


def index(request):
    """View function for home page of site."""

    question_list = Question.objects.all()

    context = {
        'question_list': question_list,

    }

    return render(request, 'index.html', context=context)



def question_detail(request, pk):
   question = get_object_or_404(Question, pk=pk)
   answers = Answer.objects.filter(question_answered=question)

   context = {
       'question': question,
       'answers': answers,

   }

   return render(request, 'core/question_detail.html', context=context)

def create_question(request):
    author = request.user
    if request.method == 'POST':
        form = AddQuestion(request.POST)
        if form.is_valid():
            question = Question.objects.create(author=author, title=form.cleaned_data['title'])
            question.save()
            return HttpResponseRedirect(reverse('question-detail', args=[question.pk]))
    else:
        form = AddQuestion()

    context = {
        'form': form,
        'author': author,
    }

    return render(request, 'core/new_question.html', context)