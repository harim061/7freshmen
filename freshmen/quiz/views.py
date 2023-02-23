from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from account.models import User

# Create your views here.

def solveQuestion(request, id):
    quiz_user = get_object_or_404(User, pk=id) # 문제 내는 사람

    if request.method == 'POST':

        print(request.POST)
        questions=QuesModel.objects.get(writer=quiz_user)
        correct=0
        total = len(questions)
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
        return render(request,'templates/quiz2/addQuestion.html',context)
    else: 
        return redirect('quiz:home') 