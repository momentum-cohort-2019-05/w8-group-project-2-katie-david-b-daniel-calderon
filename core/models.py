from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse


# Create your models here.

class Question(models.Model):
   
    title = models.CharField(max_length=200)
    ques_body = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    ques_date_added = models.DateField(auto_now_add=True)
    ques_likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-ques_date_added']
        
    def get_absolute_url(self):
        
        return reverse('index')

class Answer(models.Model):

    question_answered = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    ans_date_added = models.DateField(auto_now_add=True)
    ans_likes = models.PositiveIntegerField(default=0)
    correct = models.BooleanField(default=False)

    
    def __str__(self):
        return f"{self.question_answered}{self.text}"

    def get_absolute_url(self):
        pass
    
    class Meta:
        ordering = ['-ans_date_added']

class Star(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    star_answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE, null=True)
    star_question = models.ForeignKey(to=Question, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        if self.star_answer:
            return f"{self.user}|{self.star_question.title}|{self.star_answer[:25]}"
        else:
            return f"{self.user}|{self.star_question.title}"
