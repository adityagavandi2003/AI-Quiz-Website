from django.contrib import admin
from aiquiz.models import Quizes,Result
# Register your models here.

@admin.register(Quizes)
class QuizesAdmin(admin.ModelAdmin):
    list_display=('topic','creater','question_file','created_at')

@admin.register(Result)
class QuizesAdmin(admin.ModelAdmin):
    list_display=('marks','total_marks')