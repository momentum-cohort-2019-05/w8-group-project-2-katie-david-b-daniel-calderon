
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('question_detail/<int:pk>', views.question_detail, name='question-detail'),
    path('new_question/', views.create_question, name='new-question'),
    path('user_profile/<int:pk>', views.user_profile, name='user-profile'),
    # path('user_profile/<int:pk>', views.UserProfileView.as_view(), name='user-profile'),
    path('delete-question/<int:pk>', views.delete_question, name='delete-question'),
    path('add_answer/', views.add_answer, name='add-answer'),
    path('favorite_added/<int:pk>', views.add_to_favorites, name='favorites'),
    path('favorites/', views.user_favorites, name='user-favorites'),
    path('mark-correct/<int:answer_pk>', views.mark_correct, name='mark-correct'),

]