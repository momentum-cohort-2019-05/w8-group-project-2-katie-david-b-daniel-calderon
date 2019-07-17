from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Question(models.Model):
   
    title = models.CharField(max_length=200)
    ques_body = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    ans_correct = models.OneToOneField(to="Answer", on_delete=models.SET_NULL, null=True, blank=True) 
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
    ans_body = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    ans_date_added = models.DateField(auto_now_add=True)
    ans_likes = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.question_answered.title}{self.ans_body}"

    def get_absolute_url(self):
        pass
    
    class Meta:
        ordering = ['-ans_date_added']

class Star(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    star_answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE)
    star_question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    
    def __str__(self):
        pass
