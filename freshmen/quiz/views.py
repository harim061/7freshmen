from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from account.models import User

# Create your views here.

def solveName(request, id):
    if request.GET:
        quiz_user = get_object_or_404(User, pk=id)
        user = SolveQuiz()
        user.nickname = request.GET['nickname']
        if request.GET['name'] == "":
            user.nickname = "익명"
        user.quiz_writer = quiz_user
        return redirect("solveQuiz", user.pk)
    return render(request, "/")

def solveQuiz(request, pk):
    user = get_object_or_404(SolveQuiz, pk=pk)
    quiz_user = get_object_or_404(QuesModel, writer=user.quiz_writer)

    num = 1
    if request.POST:
        num = int(request.POST['quiz_id'])+1
        user.answer = user.answer + request.POST['answer']
        if request.POST['answer'] == quiz_user.ans[num-2]:
            user.solve_num += 1
            user.save()
        
    quiz = get_object_or_404(QuesModel, id=num)

    return render(request, "templates/quiz/QuizDetail.html", {'quiz':quiz})

def result(request, pk):
    user = get_object_or_404(SolveQuiz, pk=pk)
    total_score = user.solve_num
    return render(request, "결과 html", {"user":user, 'total_score':total_score})
    
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