from django.db import models

# Create your models here.
class QuesModel(models.Model):
    writer = models.ForeignKey('account.User',on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    op1 = models.CharField(max_length=200)
    op2 = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.id)+"번 문제"
    
class SolveQuiz(models.Model):
    nickname = models.CharField(max_length=20)
    quiz_writer = models.ForeignKey('QuesModel',on_delete=models.CASCADE)
    solve_num = models.IntegerField(default=0)
    answer = models.CharField(default="", max_length=30)

    def __str__(self):
        return self.nickname