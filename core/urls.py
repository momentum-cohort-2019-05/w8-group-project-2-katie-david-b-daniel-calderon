
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('question_detail/<int:pk>', views.question_detail, name='question-detail'),

]