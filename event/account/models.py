from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    email = models.CharField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email