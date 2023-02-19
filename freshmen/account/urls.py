from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('findid/', views.find_id, name='findid'),
    path('findpassword/', views.find_password, name='findpassword'),
]