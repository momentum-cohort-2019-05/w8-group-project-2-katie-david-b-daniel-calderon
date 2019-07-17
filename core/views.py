
from django.shortcuts import render
from core.models import Question, Answer, Star
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def index(request):
    """View function for home page of site."""

    question_list = Question.objects.all()
      
    #category_list = Category.objects.all()

    #category = Book.category



    context = {
        'question_list': question_list,
#       'category': category,
#       'category_list': category_list,
    }

    return render(request, 'index.html', context=context)