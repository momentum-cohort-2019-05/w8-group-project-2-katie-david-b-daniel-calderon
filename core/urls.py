
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('question_detail/<pk>', views.question_detail, name='question-detail'),
    path('new_question/', views.create_question, name='new-question'),
    path('user_profile/<pk>', views.user_profile, name='user-profile'),
    path('delete-question/<int:pk>', views.delete_question, name='delete-question'),


]