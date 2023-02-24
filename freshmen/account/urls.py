from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('',views.main),
    path('main2/',views.main2),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('findid/', views.find_id, name='findid'),
    path('activate/<str:uid64>/<str:token>', views.activate, name='activate'),
    path('password_reset/', views.password_reset_request, name="password_reset"),
    # path('findpassword/', views.find_password, name='findpassword'),
    path('logout/', views.logout, name='logout'),
    path('profile',views.profile,name="profile"),
]