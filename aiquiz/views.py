from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import Questions
import os
from pathlib import Path
from aiquiz.quiz_generator import generate_quiz
from aiquiz.models import Quizes,Result
from aiquiz.forms import ResultForm
import json
# Create your views here.

folder_path = r"D:\visualcode\Workspacse\Django\AI Quiz system\Questions"

@login_required
def home(request):
    user = request.user.username if request.user else 'Guest'
    history = Quizes.objects.filter(creater=user)
    if request.method == 'POST':
        search = request.POST['search']
    
        if search:
            topic = search.split(' ').pop(0)
            generate = generate_quiz(creater=user,topic=search)
            quiz_data = Quizes.objects.create(
                topic=search,
                creater=request.user.username,
                question_file = generate
            )
            quiz_data.save()
            return redirect(f'quiz/r/{quiz_data.id}')
            
    context = {
        'history':history,
    }
    return render(request,'home.html',context)


def quiz(request):
    quiz = Quizes.objects.all().order_by('-created_at')
    context = {
        'quiz':quiz,
    }
    return render(request,'quizs.html',context)

def complete_quiz(request):
    result = Result.objects.all().order_by('-created_at')
    with open('Store/python_programming_with_10_questions_aditya_2025-02-13-20-55-11.json','r') as jsonfile:
        datas = json.load(jsonfile)
    context = {
        'result':result,
    }
    return render(request,'quiz.html',context)

def quizopen(request,pk):
    filepath = Quizes.objects.get(pk=pk)

    with open(f'{filepath.question_file}','r') as jsonfile:
        data = json.load(jsonfile)

    if request.method == 'POST':
        marks = request.POST['marks']
        total_marks = request.POST['totalmarks']

        result = Result.objects.create(
            quiz=filepath,
            marks=marks,
            attempted=request.user.username,
            total_marks=total_marks
        )
        result.save()
        return redirect('quiz')
    
    context = {
        'filepath':filepath,
        'quiz':data,
    }

    return render(request,'quiztemplates.html',context)

def aboutus(request):
    return render(request,'services/aboutus.html')
