
from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    username   = models.CharField (max_length=250, unique=True)
    first_name = models.CharField (max_length=250)
    last_name  = models.CharField (max_length=250)
    email      = models.EmailField(max_length=250)

    def __str__(self):
        return f'{self.username},{self.first_name},{self.last_name}'