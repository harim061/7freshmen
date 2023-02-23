from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(required=True,max_length=20, widget=forms.TextInput(attrs={'class' :'form-control', 'placeholder' : '닉네임을 입력하세요' }))
    comment = forms.CharField(required=True,widget=forms.Textarea(attrs={'class' :'form-control', 'placeholder' : '방명록을 남겨주세요' }))

    field_order = [
        'name',
        'comment',
    ]