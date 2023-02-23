from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
    path('<int:pk>', views.solveName, name='solveName'),
    path('solveQuiz/<int:pk>', views.solveQuiz, name='solveQuiz'),
    path('addQuestion/<int:pk>', views.addQuestion, name='addQuestion'),
]