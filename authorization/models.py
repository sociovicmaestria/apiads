from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    activate = models.BooleanField(default=True)    

    class Meta:
        ordering = ('username',)