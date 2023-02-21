from django.shortcuts import render, redirect
from .models import User, Profile
from argon2 import PasswordHasher
from .forms import SignupForm, LoginForm, ProfileForm, FindIdForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def signup(request):
    signup_form = SignupForm()
    context = {'forms':signup_form}

    if request.method == 'GET':
        return render(request, 'templates/account/Sign.html', context)
    
    elif request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            # user.set_password(signup_form.cleaned_data['user_pw'])
            user = User(
                user_id = signup_form.user_id,
                password = signup_form.user_pw,
                username = signup_form.username
            )
            user.save()
            return render(request,'templates/account/Sign.html',{'user':user})
        else:
            context['forms']=signup_form
            if signup_form.errors:
                for value in signup_form.errors.values():
                    context['error'] = value
        return render(request, 'templates/account/Sign.html', context)

def login(request):
    loginform = LoginForm()
    context = {'forms':loginform}

    if request.method == 'GET':
        return render(request,'templates/account/login.html',context)
    
    elif request.method=='POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            return redirect('/')
        else:
            context['forms'] = loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error'] = value
        return render(request, 'templates/account/login.html', context)
    
@login_required
def profile(request):
    if request.method == 'POST':
        profileForm = ProfileForm(request.POST, request.FILES,instance=request.user.profile)

        if profileForm.is_valid():
            profileForm.save()
            return redirect('/')
    else:
        profileForm = ProfileForm(instance=request.user.profile)

    context = {'forms':profileForm}

    return render(request,'templates/account/profile.html',context)

def find_id(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            context = {}
            user = User.objects.get(username=username)
            if user is not None:
                id = user.user_id
                context = {'id':id}
                return render(request, 'templates/account/accountfindid.html', context)
        except:
            messages.error(request, '존재하지 않는 닉네임입니다.')
    context={}
    return render(request,'templates/account/findid.html',context)

def find_password(request):
    context = {}
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        try:
            context = {}
            user = User.objects.get(user_id=user_id)
            if user is not None:
                password = user.password
                context = {'password':password}
                return render(request, 'templates/account/findpassword.html', context)
        except:
            messages.error(request, '존재하지 않는 아이디입니다.')
    context={}
    return render(request,'templates/account/findpassword.html',context)