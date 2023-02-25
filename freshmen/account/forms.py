from django import forms
from .models import User, Profile
from argon2 import PasswordHasher, exceptions
from django.contrib.auth.hashers import make_password, check_password

# 회원가입 폼
class SignupForm(forms.ModelForm):
    user_id = forms.EmailField(
        label='아이디',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class' : 'user-id',
                'placeholder' : '아이디'
            }
        ),
        error_messages={'required':'아이디를 입력해주세요.',
        'unique':'중복된 아이디입니다.'}
    )

    user_pw = forms.CharField(
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pw',
                'placeholder' : '비밀번호'
            }
        ),
        error_messages={'required':'비밀번호를 입력해주세요.'}
    )

    user_pw_confirm = forms.CharField(
        label='비밀번호 확인',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pw-confirm',
                'placeholder' : '비밀번호 확인'
            }
        ),
        error_messages={'required':'비밀번호를 한번 더 입력해주세요.'}
    )

    username = forms.CharField(
        label='닉네임',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'username',
                'placeholder' : '닉네임'
            }
        ),
        error_messages={'required':'닉네임을 입력해주세요.'}
    )

    field_order = [
        'username',
        'user_id',
        'user_pw',
        'user_pw_confirm'
    ]

    class Meta:
        model = User
        fields = [
            'username','user_id','user_pw','user_pw_confirm'
        ]
    
    def clean(self):
        cleaned_data = super().clean()

        user_id = cleaned_data.get('user_id','')
        user_pw = cleaned_data.get('user_pw','')
        user_pw_confirm = cleaned_data.get('user_pw_confirm','')
        username = cleaned_data.get('username','')

        if user_pw != user_pw_confirm:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        else:
            self.user_pw = make_password(user_pw)
            self.user_id = user_id
            # self.user_pw = PasswordHasher().hash(user_pw)
            self.user_pw_confirm = user_pw_confirm
            self.username = username

# 로그인 폼
class LoginForm(forms.Form):
    user_id = forms.EmailField(
        max_length=32,
        label='아이디',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class' : 'user-id',
                'placeholder' : '아이디'
            }
        ),
        error_messages={'required' : '아이디를 입력해주세요.'}
    )

    user_pw =  forms.CharField(
        max_length=128,
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pw',
                'placeholder' : '비밀번호'
            }
        ),
        error_messages={'required' : '비밀번호를 입력해주세요.'}
    )

    field_order = [
        'user_id',
        'user_pw',
    ]

    def clean(self):
        cleaned_data = super().clean()

        user_id = cleaned_data.get('user_id','')
        user_pw = cleaned_data.get('user_pw','')

        if user_id == '':
            return self.add_error('user_id','아이디를 다시 입력해주세요.')
        elif user_pw == '':
            return self.add_error('user_pw','비밀번호를 다시 입력해주세요.')
        else:
            try:
                user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                return self.add_error('user_id','아이디가 존재하지 않습니다.')
            
            self.usr = user_id
            self.pwd = user_pw

            try:
                # PasswordHasher().verify(user.password,user_pw)
                check_password(user.password, user_pw)
            # except exceptions.VerifyMismatchError:
            except Exception:
                self.pwd = 0
                return self.add_error('user_pw', '비밀번호가 일치하지 않습니다.')

# 프로필 폼
class ProfileForm(forms.ModelForm):
    school = forms.CharField(
        max_length=128,
        label='학교',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'school',
                'placeholder' : '학교'
            }
        ),
        error_messages={'required' : '학교를 입력해주세요.'}
    )

    major = forms.CharField(
        max_length=128,
        label='전공',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'major',
                'placeholder' : '전공'
            }
        ),
        error_messages={'required' : '전공/학부를 입력해주세요.'}
    )

    gender = forms.ChoiceField(
        label='성별',
        required=True,
        choices=Profile.GENDER_CHOICES,
        error_messages={'required' : '성별을 선택해주세요.'}
    )

    mbti = forms.ChoiceField(
        label='MBTI',
        required=True,
        choices=Profile.MBTI_CHOICES,
        error_messages={'required' : 'MBTI를 선택해주세요.'}
    )

    age = forms.IntegerField(
        label='나이',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'age',
                'placeholder' : '나이'
            }
        ),
        error_messages={'required' : '나이를 입력해주세요.'}
    )

    live = forms.ChoiceField(
        label='자취유무',
        choices=Profile.LIVE_CHOICES,
    )

    favfood = forms.CharField(
        max_length=128,
        label='음식',
        widget=forms.TextInput(
            attrs={
                'class' : 'favfood',
                'placeholder' : '내가 선호하는 음식은?'
            }
        )
    )

    drink = forms.CharField(
        max_length=128,
        label='주량',
        widget=forms.TextInput(
            attrs={
                'class' : 'drink',
                'placeholder' : '나의 주량은?'
            }
        )
    )

    hometown = forms.CharField(
        max_length=128,
        label='고향',
        widget=forms.TextInput(
            attrs={
                'class' : 'hometown',
                'placeholder' : '나의 고향은?'
            }
        )
    )
    
    image = forms.ImageField(
        label = '프로필 이미지',
    )

    timetable = forms.ImageField(
        label = '시간표',
    )

    field_order = [
        'school',
        'major',
        'gender',
        'mbti',
        'age',
        'live',
        'favfood',
        'drink',
        'hometown',
        'image',
        'timetable',
    ]

    class Meta:
        model = Profile
        fields = [
            'school','major','gender','mbti','age','image',
            'live','favfood','drink','hometown','timetable',
        ]

    # def clean(self):
    #     cleaned_data = super().clean()

    #     self.school = cleaned_data.get('school','')
    #     self.major = cleaned_data.get('major','')
    #     self.gender = cleaned_data.get('gender','')
    #     self.mbti = cleaned_data.get('mbti','')
    #     self.age = cleaned_data.get('age','')

    #     self.live = cleaned_data.get('live','')
    #     self.favfood = cleaned_data.get('favfood','')
    #     self.drink = cleaned_data.get('drink','')
    #     self.hometown = cleaned_data.get('hometown','')