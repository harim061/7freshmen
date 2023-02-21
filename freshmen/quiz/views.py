from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            if q.ans ==  request.POST.get(q.question):
                correct+=1
        context = {
            'correct':correct,
            'total':total
        }
        return render(request,'templates/result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'templates/home.html',context)
    
def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionForm()
        if(request.method=='POST'):
            form=addQuestionForm(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'templates/addQuestion.html',context)
    else: 
        return redirect('home') 