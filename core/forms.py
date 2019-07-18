from django import forms
from core.models import Question, Answer, Star


class AddQuestion(forms.Form):
    title = forms.CharField(max_length=100, help_text='Enter a title for the question.')
    question = forms.CharField(widget=forms.Textarea, help_text='Enter a description of your question.')
    