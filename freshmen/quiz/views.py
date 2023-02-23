from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

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
        return render(request,'templates/quiz2/result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'templates/quiz2/home.html',context)
    
def addQuestion(request):    
        return render(request,'templates/home.html',context)

@login_required()
def addQuestion(request):
    if request.user.is_staff:
        quizform=addQuestionForm()
        context= {'quizform':quizform}

        if request.method=='POST':
            quizform=addQuestionForm(request.POST)
            if quizform.is_valid():
                quiz = quizform.save(commit=False)
                quiz.writer = request.user
                quiz.save()
                return redirect('/')
        context={'quizform':quizform}
        return render(request,'templates/addQuestion.html',context)
    else: 
        return redirect('quiz:home') 