from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
    path('<int:pk>', views.solveName, name='solveName'),
    path('solveQuiz/<int:pk>', views.solveQuiz, name='solveQuiz'),
    path('addQuestion/', views.addQuestion, name='addQuestion'),
    path('showresult/<int:pk>', views.each_result, name='eachresult'),
    path('result/<int:pk>',views.result, name='result'),
]