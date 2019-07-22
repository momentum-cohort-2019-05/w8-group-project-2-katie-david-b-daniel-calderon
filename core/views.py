
from django.shortcuts import render
from core.models import Question, Answer, Star
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import AddQuestionForm, AddAnswerForm
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
            q = question.pk
            return HttpResponseRedirect(reverse('question-detail', args=[q]))
    else:
        form = AddQuestionForm()

    context = {
        'form': form,
        'author': author,
    }

    return render(request, 'core/new_question.html', context)

@login_required
def add_answer(request):
    author = request.user
    if request.method == 'POST':
        form = AddAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            return HttpResponseRedirect(reverse('question-detail', args=[answer.question_answered_id]))
    else:
        form = AddAnswerForm()
        
    context = {
        'form': form,
        'author': author,
    }

    return render(request, 'core/add_answer.html', context)

@login_required
def user_profile(request, pk):

    all_questions = Question.objects.all()
    # question_list = all_questions.filter(author=request.user)
    question_list = all_questions.filter(author__pk=pk)
    author_list = all_questions.filter(author__pk=pk)
        
    context = {
        'question_list': question_list,
        'author_list': author_list,
    }
    # question = Question.objects.get(pk=pk)
    # if request.user == question.author:
    #     all_questions = Question.objects.all()
    #     question_list = all_questions.filter(author__pk=pk)
    return render(request, 'core/user_profile.html', context)


@login_required
def delete_question(request, pk):
    """deletes a question"""
    question = Question.objects.get(pk=pk)
    if request.user == question.author:
        question.delete()
    return redirect(to='index')


@login_required
def add_to_favorites(request, pk):
    question = get_object_or_404(Question, pk=pk)

    new_favorite, created = Favorite.objects.get_or_create(
        question=question, favorited_by=request.user)
    if not created:
        new_favorite.delete()

    context = {
        'question': question,
        'new_favorite': new_favorite,
        'created': created,
    }

    return render(request, 'core/favorite_added.html', context)

@login_required
def user_favorites(request):
    favorites = Favorite.objects.filter(favorited_by=request.user)

    favorites_list = []

    for favorite in favorites:
        favorites_list.append(favorite.question)

    context = {
        'favorites': favorites,
        'favorites_list': favorites_list,
    }

    return render(request, 'core/added_favorites.html', context)

# class UserProfileView(generic.ListView):
#     model = Question
#     template_name = 'core/user_profile.html'

#     def get_queryset(self):
#         """
#         Return list of Question objects created by User (owner id specified in URL)
#         """
#         id = self.kwargs['pk']
#         author = get_object_or_404(User, pk=id)
#         return Question.objects.filter(author=target_author)

#     def get_context_data(self, **kwargs):
#         """
#         Add question owner to context so they can be displayed in the template
#         """
#         # Call the base implementation first to get a context
#         context = super(UserProfileView, self).get_context_data(**kwargs)
#         # Get the owner object from the "pk" URL parameter and add it to the context
#         context['author'] = get_object_or_404(User, pk=self.kwargs['pk'])
#         return context