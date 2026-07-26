from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    nickname = models.CharField(
        max_length=30,
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nickname