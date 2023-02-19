from django.urls import path
from . import views

app_name = 'guestbook'
urlpatterns = [
    path('index/', views.guestbook, name='guestbook'),
    path('sign/', views.index, name='index'),
]