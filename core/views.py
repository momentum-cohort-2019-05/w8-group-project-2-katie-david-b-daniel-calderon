
from django.shortcuts import render
from core.models import Question, Answer, Star
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import AddQuestionForm, AddAnswerForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
from django.core.mail import send_mail
from django.conf import settings







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
    form = AddAnswerForm

    # author = request.user
    # if request.method == 'POST':
    #     form = AddAnswerForm(request.POST)
    #     if form.is_valid():
    #         answer = form.save()
    #         return HttpResponseRedirect(reverse('question-detail', args=[answer.question_answered_id]))
    # else:
    #     form = AddAnswerForm()
            
     
    context = {
        'question': question,
        'answers': answers,
        'answer': answer,
        'form': form,
        # 'author': author,

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

# @login_required
# def add_answer(request):
#     author = request.user
#     if request.method == 'POST':
#         form = AddAnswerForm(request.POST)
#         if form.is_valid():
#             answer = form.save()
#             return HttpResponseRedirect(reverse('question-detail', args=[answer.question_answered_id]))
#     else:
#         form = AddAnswerForm()
        
#     context = {
#         'form': form,
#         'author': author,
#     }

#     # return render(request, 'core/add_answer.html', context)
#     return render(request, 'core/question_detail.html', context=context)

@login_required
def add_answer(request):
    if request.method == 'POST':
        answer_text = request.POST.get('the_answer')
        question_id = int(request.POST.get('the_question'))
        question_answered = get_object_or_404(Question, pk=question_id)
        response_data = {}

        answer = Answer(text=answer_text, author=request.user, question_answered=question_answered)
        answer.save()

        response_data['result'] = 'Create answer successful!'
        response_data['postpk'] = answer.pk
        response_data['question_answered'] = answer.question_answered.pk
        response_data['text'] = answer.text
        response_data['created'] = answer.ans_date_added.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = answer.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

        # subject = "Answer Added"
        # message = "Someone submitted an answer to your question!"
        # email_from = questionbox@gquestionbox.com
        # recipient_list = 
        # send_mail(subject, message, email_from, recipient_list)


@login_required
def user_profile(request, pk):

    all_questions = Question.objects.all()
    # question_list = all_questions.filter(author=request.user)
    question_list = all_questions.filter(author__pk=pk)
    author_list = all_questions.filter(author__pk=pk)
    all_star_ques = Star.objects.all()
    star_list = all_star_ques.filter(star_question__pk=pk)
        
    context = {
        'question_list': question_list,
        'author_list': author_list,
        'star_list': star_list,
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

    new_star, created = Star.objects.get_or_create(
        star_question=question, user=request.user)
    if not created:
        new_star.delete()

    context = {
        'question': question,
        'new_star': new_star,
        'created': created,
    }

    return render(request, 'core/favorite_added.html', context)

@login_required
def user_favorites(request):
    stars = Star.objects.filter(favorited_by=request.user)

    stars_list = []

    for star in stars:
        stars_list.append(favorite.question)

    context = {
        'stars': stars,
        'stars_list': stars_list,
    }

    return render(request, 'core/added_favorites.html', context)

def mark_correct(request, answer_pk):
    answer = Answer.objects.get(pk=answer_pk)
    current_state = answer.correct
    answer.correct = not current_state
    question = answer.question_answered
    context = {
        'question': question,
    }
    
    return render(request, 'core/question_detail.html', context=context)

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