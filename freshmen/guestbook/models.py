from django.db import models
from django.utils import timezone
from account.models import User

# Create your models here.
class Comment(models.Model):
    person = models.ForeignKey('account.User',on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

