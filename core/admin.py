from django.contrib import admin
from core.models import Question, Answer, Star

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
admin.site.register(Answer)
admin.site.register(Star)
