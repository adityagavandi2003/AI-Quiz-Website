from django.urls import path
from aiquiz import views


urlpatterns = [
    path('',views.home,name='home'),
    path('quiz/',views.quiz,name='quiz'),
    # path('results/',views.result,name='result'),
    path('quiz/results/',views.complete_quiz,name='completequiz'),
    path('quiz/r/<str:pk>',views.quizopen,name='quizopen'),
]
