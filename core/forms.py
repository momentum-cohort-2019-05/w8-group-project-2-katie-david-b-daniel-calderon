from django import forms
from django.forms import ModelForm
from core.models import Question, Answer, Star


# class AddQuestion(forms.Form):
#     title = forms.CharField(max_length=100, help_text='Enter a title for the question.')
#     question = forms.CharField(widget=forms.Textarea, help_text='Enter a description of your question.')

class AddQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'ques_body', 'author']

class AddAnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['question_answered', 'ans_body', 'author']
