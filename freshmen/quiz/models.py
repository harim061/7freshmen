from django.db import models

# Create your models here.
class QuesModel(models.Model):
    writer = models.ForeignKey('account.User',on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    op1 = models.CharField(max_length=200)
    op2 = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question