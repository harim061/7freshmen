from audioop import reverse
from django.shortcuts import render,redirect,get_object_or_404

from account.models import User
from .models import Comment
from .forms import CommentForm

# Create your views here.
# def guestbook(request, pk):
#     #author= request.user
#     comments = Comment.objects.order_by("-date_added")
#     #user = Comment.objects.filter(author)
#     context = {'comments' : comments}
#     return render(request,'templates/guestBook/guestbook.html',context)

def guestbook(request, pk):
    comments = Comment.objects.filter(person=pk)
    user = get_object_or_404(User, pk=pk)
    user_name = user.username
    context = {'comments':comments, 'name':user_name,'pk':pk}

    return render(request,'templates/guestBook/guestbook.html', context)

# def index(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             new_comment = Comment(name=request.POST['name'],comment=request.POST['comment'])
#             # new_comment.person = get_object_or_404(User, pk=user_id)
#             new_comment.save()
#         return redirect('guestbook:guestbook')
#     else:
#         form = CommentForm(request.POST)
#         context = {'comment':CommentForm}
#     return render(request,'templates/guestbook/sign.html',context)

def add_comment(request, pk):
    main_user = get_object_or_404(User, pk=pk) # 방명록 주인
    main_user_name = main_user.username # html에서 이렇게 사용

    form = CommentForm()
    context = {'username' : main_user_name, 'pk':main_user.pk,'form':form}

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment()
            new_comment.name = form.cleaned_data['name']
            new_comment.comment = form.cleaned_data['comment']
            new_comment.person = main_user
            new_comment.save()
        return redirect('guestbook:guestbook',pk=pk)

    return render(request, 'templates/guestbook/sign.html',context)
