from django import forms
from .models import *

class addQuestionForm(forms.ModelForm):
    question = forms.CharField(
        label = '문제',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'question',
                'placeholder' : '문제'
            }
        )
    )
    
    op1 = forms.CharField(
        label = '답변1',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'option1',
                'placeholder' : '답변1'
            }
        )
    )
    
    op2 = forms.CharField(
        label = '답변2',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'option2',
                'placeholder' : '답변2'
            }
        )
    )

    field_order = [
        'question',
        'op1',
        'op2',

    ]

    class Meta:
        model = QuesModel
        fields = [
            'question',
            'op1',
            'op2'
        ]
        exclude = ['writer']

    def clean(self):
        cleaned_data = super().clean()

        question = cleaned_data.get('question','')
        op1 = cleaned_data.get('op1','')
        op2 = cleaned_data.get('op2','')
        ans = cleaned_data.get('op1','')

        self.question = question
        self.op1 = op1
        self.op2 = op2
        self.ans = ans