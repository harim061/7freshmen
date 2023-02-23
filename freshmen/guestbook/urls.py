from django.urls import path
from . import views

app_name = 'guestbook'
urlpatterns = [
    path('<int:pk>',views.guestbook),
    path('guestbook/<int:pk>', views.guestbook, name='guestbook'),
    path('addcomment/<int:pk>', views.add_comment, name='add_comment'),
]