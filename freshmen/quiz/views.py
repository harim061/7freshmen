from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from account.models import User
import random

# Create your views here.

def solveName(request, pk):
    if request.POST:
        quiz_user = get_object_or_404(User, pk=pk)
        user = SolveQuiz()
        user.nickname = request.POST['nickname']
        if request.POST['nickname'] == "":
            user.nickname = "익명"
        quiz = get_object_or_404(QuesModel, writer=quiz_user)
        user.quiz_writer = quiz
        user.save()
        return redirect("quiz:solveQuiz", user.pk)
    return render(request, "templates/quiz2/GuessQ.html")
    
def solveQuiz(request, pk):
    user = SolveQuiz.objects.get(pk=pk)
    quiz_writer = user.quiz_writer

    question = []
    op1 = []
    op2 = []
    quizs = []
    i=2
    while True:
        question.append(quiz_writer.question[i])
        op1.append(quiz_writer.op1[i])
        op2.append(quiz_writer.op2[i])
        i += 5
        if i>22:
            break
    
    for i in range(0,5):
        quiz = []
        quiz.append(op1[i])
        quiz.append(op2[i])
        random.shuffle(quiz)

        quiz.append(question[i])
        quizs.append(quiz)
    
    random.shuffle(quizs)

    context = {'quizs':quizs, 'pk': pk}

    num = len(user.answer)
    if request.POST:
        user.answer = user.answer + request.POST['answer']
        if request.POST['answer'] == quiz_writer.ans[num]:
            user.solve_num += 1
            user.save()
        return render(request, "templates/quiz/QuizDetail.html", context)
    return render(request, "templates/quiz/QuizDetail.html", context)

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