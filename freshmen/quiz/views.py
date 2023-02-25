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
    return render(request, "templates/quiz2/GuessQ.html", {'pk':pk})
    
def solveQuiz(request, pk):
    user = SolveQuiz.objects.get(pk=pk)
    quiz_writer = user.quiz_writer

    question = []
    op1 = []
    op2 = []
    quizs = []

    q = quiz_writer.question
    p1 = quiz_writer.op1
    p2 = quiz_writer.op2

    a = q.find(',')
    question.append(q[2:a-1]) # 1번 문제
    q = q[a+3:]

    b = p1.find(',')
    op1.append(p1[2:b-1]) # 1번 문제
    p1 = p1[b+3:]

    c = p2.find(',')
    op2.append(p2[2:c-1]) # 1번 문제
    p2 = p2[c+3:]

    for j in range(0,3):
        a = q.find(',')
        question.append(q[:a-1]) # 2번, 3번, 4번 문제
        q = q[a+3:]

        b = p1.find(',')
        op1.append(p1[:b-1]) # 2번, 3번, 4번 문제
        p1 = p1[b+3:]

        c = p2.find(',')
        op2.append(p2[:c-1]) # 2번, 3번, 4번 문제
        p2 = p2[c+3:]
        
    question.append(q[:-2])
    op1.append(p1[:-2])
    op2.append(p2[:-2])
    
    for i in range(0,5):
        quiz = []
        quiz.append(op1[i])
        quiz.append(op2[i])
        random.shuffle(quiz)

        quiz.append(question[i])
        quizs.append(quiz)

    context = {'quiz1':quizs[0], 'quiz2':quizs[1], 'quiz3':quizs[2], 'quiz4':quizs[3], 'quiz5':quizs[4], 'pk': pk}

    if request.POST:
        answer1 = request.POST['answer1']
        answer2 = request.POST['answer2']
        answer3 = request.POST['answer3']
        answer4 = request.POST['answer4']
        answer5 = request.POST['answer5']
        answer = []
        answer.append(answer1)
        answer.append(answer2)
        answer.append(answer3)
        answer.append(answer4)
        answer.append(answer5)
        for i in range(0,5):
            if answer[i] == op1[i]:
                user.solve_num += 1
        user.save()
        return render(request, "templates/quiz2/result.html", {'solve_num':user.solve_num})
    return render(request, "templates/quiz/QuizDetail.html", context)

def result(request, pk):
    user = get_object_or_404(SolveQuiz, pk=pk)
    total_score = user.solve_num
    return render(request, "templates/quiz2/result.html", {"user":user, 'total_score':total_score})
    
def each_result(request, pk):
    results = get_object_or_404(SolveQuiz, quiz_writer = pk)
    nickname = results.nickname
    score = results.solve_num

    return render(request, "templates/quiz2/QuizResult.html", {"nickname":nickname, 'score':score})

@login_required()
def addQuestion(request):
    if request.user.is_active:
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