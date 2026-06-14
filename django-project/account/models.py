from django.db import models
from django.contrib.auth.models import AbstractUser 

class CustomUser(AbstractUser):
    nickname = models.CharField(
        max_length=50,
        help_text="화면에 노출될 익명 닉네임입니다."
    )
#CharField - 유저 ID, 비밀번호, 익명 닉네임, 활동 중인지, 직원인지, 