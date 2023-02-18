from django.shortcuts import render, redirect
from .models import User, Profile
from argon2 import PasswordHasher
from .forms import SignupForm, LoginForm, ProfileForm

# Create your views here.
def signup(request):
    signup_form = SignupForm()
    context = {'forms':signup_form}

    if request.method == 'GET':
        return render(request, 'account/signup.html', context)
    
    elif request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.set_password(signup_form.cleaned_data['user_pw'])
            user.save()
            return render(request,'account/signup.html',{'user':user})
        else:
            context['forms']=signup_form
            if signup_form.errors:
                for value in signup_form.errors.values():
                    context['error'] = value
        return render(request, 'account/signup.html', context)

def login(request):
    loginform = LoginForm()
    context = {'forms':loginform}

    if request.method == 'GET':
        return render(request,'account/login.html',context)
    
    elif request.method=='POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            return redirect('/')
        else:
            context['forms'] = loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error'] = value
        return render(request, 'account/login.html', context)