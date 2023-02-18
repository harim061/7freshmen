from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, BaseUserManager
from PIL import Image
# Create your models here.

# 초기 회원가입 시 유저 모델

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self,user_id,username,password,**extra_fields):
        if not user_id:
            raise ValueError('아이디를 입력해주세요.')
        if not username:
            raise ValueError('닉네임을 입력해주세요.')
        if not password:
            raise ValueError('비밀번호를 입력해주세요.')
        
        username = self.model.normalize_username(username)
        user = self.model(
            user_id = user_id,
            username = username,
            **extra_fields
        )
        user.set_password(password)
        user.save (using=self._db)
        return user
    
    def create_user(self,user_id,username,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(user_id,username,password,**extra_fields)
    
    def create_superuser(self,user_id,username,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')
        
        return self._create_user(user_id,username,password,**extra_fields)
    
class User(AbstractUser):
    user_id = models.CharField(max_length=32, unique=True, verbose_name='아이디')
    username = models.CharField(max_length=32, verbose_name='닉네임', unique=True)
    objects = UserManager()
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.user_id

class Profile(models.Model):

    GENDER_CHOICES = {
        ('male','남성'),
        ('female','여성'),
    }

    MBTI_CHOICES = {
        ('ESTJ','ESTJ'),
        ('ESTP','ESTP'),
        ('ESFJ','ESFJ'),
        ('ESFP','ESFP'),
        ('ENTJ','ENTJ'),
        ('ENTP','ENTP'),
        ('ENFJ','ENFJ'),
        ('ENFP','ENFP'),
        ('ISTJ','ISTJ'),
        ('ISTP','ISTP'),
        ('ISFJ','ISFJ'),
        ('ISFP','ISFP'),
        ('INTJ','INTJ'),
        ('INTP','INTP'),
        ('INFJ','INFJ'),
        ('INFP','INFP'),
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=128, null=True, blank=False)
    major = models.CharField(max_length=128, null=True, blank=False)
    gender = models.CharField(max_length=16, choices=GENDER_CHOICES, null=True)
    mbti = models.CharField(max_length=16, choices=MBTI_CHOICES, null=True)
    age = models.IntegerField(null=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile/', default='default.jpg')

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save,sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)