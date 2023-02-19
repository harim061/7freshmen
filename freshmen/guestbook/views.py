from django.shortcuts import render,redirect,get_object_or_404

from account.models import User
from .models import Comment
from .forms import CommentForm

# Create your views here.
def guestbook(request):
    comments = Comment.objects.order_by("-date_added")

    context = {'comments' : comments}
    return render(request,'guestbook/index.html',context)

def index(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(name=request.POST['name'],comment=request.POST['comment'])
            # new_comment.person = get_object_or_404(User, pk=user_id)
            new_comment.save()
        return redirect('home')
    else:
        form = CommentForm()
    context = {'form' : form}
    return render(request,'guestbook/sign.html',context)