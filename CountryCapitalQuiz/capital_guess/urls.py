from django.urls import path
from capital_guess import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play_quiz/', views.play_quiz, name='play_quiz'),
    path('check_guess/', views.check_guess, name='check_guess'),
    path('get_new_question/', views.get_new_question, name='get_new_question'),
]
