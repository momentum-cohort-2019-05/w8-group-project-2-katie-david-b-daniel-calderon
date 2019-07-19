
from django.shortcuts import render
from core.models import Question, Answer, Star
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import AddQuestionForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



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
   answer = question.answer_set.all()


   context = {
       'question': question,
       'answers': answers,
       'answer': answer,

   }

   return render(request, 'core/question_detail.html', context=context)

@login_required
def create_question(request):
    author = request.user
    if request.method == 'POST':
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(reverse('question-detail', args=[question.pk]))
    else:
        form = AddQuestionForm()

    context = {
        'form': form,
        'author': author,
    }

    return render(request, 'core/new_question.html', context)

@login_required
def user_profile(request, pk):

    all_questions = Question.objects.all()
    question_list = all_questions.filter(pk=pk)
        
    context = {
        'question_list': question_list
    }
    
    return render(request, 'core/user_profile.html', context)

@login_required
def delete_question(request, pk):
    """deletes a question"""
    question = Question.objects.get(pk=pk)
    if request.user == question.author:
        question.delete()
    return redirect(to='index', pk=request.user.pk)