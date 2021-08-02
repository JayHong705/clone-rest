from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import UserDefaultManager, ProfileDefaultManager


class User(AbstractBaseUser):
    """
    가독성을 위해 명시적으로 user 모델 정의
    """
    identifier = models.CharField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'identifier'

    objects = UserDefaultManager()

    def __str__(self):
        return self.identifier


class Profile(models.Model):
    """
    intro, topic, profile_image 등이 추가되어야 할
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text="유저")
    name = models.CharField(max_length=30, blank=True, help_text="닉네임(영어/온전한 한글만 가능)")
    device_token = models.CharField(max_length=1023, blank=True, help_text='푸시 알람 보낼 때 쓰는 디바이스 토큰')

    objects = ProfileDefaultManager()