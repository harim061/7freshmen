from django.forms import ModelForm
from .models import *

class addQuestionForm(ModelForm):
    class Meta:
        model = QuesModel
        fields = "__all__"