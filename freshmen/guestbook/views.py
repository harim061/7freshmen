from django.shortcuts import render,redirect,get_object_or_404

from account.models import User
from .models import Comment
from .forms import CommentForm

# Create your views here.
def guestbook(request):
    author = request.user
    comments = Comment.objects.order_by("-date_added")
    user = Comment.objects.filter(author=author)
    context = {'comments' : comments,'user':user}
    return render(request,'templates/guestBook/guestbook.html',context)

def index(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(name=request.POST['name'],comment=request.POST['comment'])
            # new_comment.person = get_object_or_404(User, pk=user_id)
            new_comment.save()
        return redirect('guestbook:guestbook')
    else:
        form = CommentForm(request.POST)
        context = {'comment':CommentForm}
    return render(request,'templates/guestbook/sign.html',context)