from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from account.models import User

# Create your views here.

def solveName(request, pk):
    if request.GET:
        quiz_user = get_object_or_404(User, pk=pk)
        user = SolveQuiz()
        user.nickname = request.GET['nickname']
        if request.GET['nickname'] == "":
            user.nickname = "익명"
        user.quiz_writer = quiz_user
        user.save()
        return redirect("solveQuiz", user.pk)
    return render(request, "templates/quiz2/GuessQ.html")
    
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

    return render(request, "templates/quiz/QuizNum.html", {'quiz':quiz})

def result(request, pk):
    user = get_object_or_404(SolveQuiz, pk=pk)
    total_score = user.solve_num
    return render(request, "결과 html", {"user":user, 'total_score':total_score})
    
def each_result(request, pk):
    results = get_object_or_404(SolveQuiz, quiz_writer = pk)
    nickname = results.nickname
    score = results.solve_num

    return render(request, "사람 마다 결과값", {"nickname":nickname, 'score':score})

@login_required()
def addQuestion(request):
    if request.user.is_staff:
        quizform=addQuestionForm()
        context= {'quizform':quizform}

        if request.method=='POST':
            quiz = QuesModel.objects.create(writer = request.user,question = request.POST.getlist("question[]"),op1 = request.POST.getlist("op1[]"),op2 = request.POST.getlist("op2[]"))
            quiz.save()

            return render(request,'templates/quiz2/MakeQComplete.html', context)


        context={'quizform':quizform}
        return render(request,'templates/quiz2/makeQ.html', context)
    else: 
        return redirect('quiz:home') 