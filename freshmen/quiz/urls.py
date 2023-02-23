from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
    path('solveQuestion/', views.solveQuestion, name='solveQuestion'),
    path('addQuestion/', views.addQuestion, name='addQuestion'),
]