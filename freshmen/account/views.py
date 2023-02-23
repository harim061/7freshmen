from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import User, Profile
from argon2 import PasswordHasher
from .forms import SignupForm, LoginForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_str
from django.urls import reverse_lazy

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings


def main(request):
    return render(request,'templates/main.html')
def main2(request):
    return render(request,'templates/main2.html')
# Create your views here.
def signup(request):
    signup_form = SignupForm()
    context = {'forms':signup_form}

    if request.method == 'GET':
        return render(request, 'templates/account/sign_up.html', context)
    
    elif request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user = User(
                user_id = signup_form.user_id,
                username = signup_form.username,
                password = signup_form.user_pw
            )
            # user.password = PasswordHasher(signup_form.user_pw)
            user.is_active = False
            user.save()
            current_site = get_current_site(request) 
            # localhost:8000
            message = render_to_string('templates/account/user_activate_email.html',                         {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = "[친해지길 바라] 회원가입 인증 메일입니다."
            email = EmailMessage(mail_subject, message, to=[signup_form.user_id])
            email.send()
            return HttpResponse(
                '<div style="font-size: 40px; width: 100%; height:100%; display:flex; text-align:center; '
                'justify-content: center; align-items: center;">'
                '입력하신 이메일<span>로 인증 링크가 전송되었습니다.</span>'
                '</div>'
            )
            return render(request,'templates/account/Sign.html',{'user':user})
        else:
            context['forms']=signup_form
            if signup_form.errors:
                for value in signup_form.errors.values():
                    context['error'] = value
        return render(request, 'templates/account/sign_up.html', context)

def activate(request, uid64, token):

    uid = force_str(urlsafe_base64_decode(uid64))
    user = User.objects.get(pk=uid)

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request,'templates/account/log_in.html')
    else:
        return HttpResponse('비정상적인 접근입니다.')

def login(request):
    loginform = LoginForm()
    context = {'forms':loginform}

    if request.method == 'GET':
        return render(request,'templates/account/log_in.html',context)
    
    elif request.method=='POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            request.session['login_session'] = loginform.login_session
            request.session.set_expiry(0)
            return render(request,'templates/account/profile.html',context)
        else:
            context['forms'] = loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error'] = value
        return render(request, 'templates/account/log_in.html', context)
    
@login_required
def profile(request):
    if request.method == 'POST':
        profileForm = ProfileForm(request.POST, request.FILES,instance=request.user.profile)

        if profileForm.is_valid():
            profileForm.save()
            return render(request,'templates/account/profile.html',context)
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

# def find_password(request):
#     context = {}
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')
#         try:
#             context = {}
#             user = User.objects.get(user_id=user_id)
#             if user is not None:
#                 password = user.password
#                 context = {'password':password}
#                 return render(request, 'templates/account/findpassword.html', context)
#         except:
#             messages.error(request, '존재하지 않는 아이디입니다.')
#     context={}
#     return render(request,'templates/account/findpassword.html',context)

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = get_object_or_404(User,user_id=data)
			if associated_users.exists():
				for user in associated_users:
					subject = '[친해지길 바라] 비밀번호 재설정'
					email_template_name = "account/password_reset_email.txt"
					c = {
						"email": user.user_id,
						# local: '127.0.0.1:8000', prod: 'givwang.herokuapp.com'
						'domain': settings.HOSTNAME,
						'site_name': 'givwang',
						# MTE4
						"uid": urlsafe_base64_encode(force_bytes(user.pk)),
						"user": user,
						# Return a token that can be used once to do a password reset for the given user.
						'token': default_token_generator.make_token(user),
						# local: http, prod: https
						'protocol': settings.PROTOCOL,
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'givwang.official@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(
		request=request,
		template_name='account/password_reset.html',
		context={'password_reset_form': password_reset_form})

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('account:login')

def logout(request):
    request.session.flush()
    return redirect('/')

# 로그인 상태인지 확인하는 view
def check_login(request):
    context = {}

    login_session = request.session.get('login_session','')

    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True

    return render(request, '홈 연결 링크 넣어주세요 !', context)