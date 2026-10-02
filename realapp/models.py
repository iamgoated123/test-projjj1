from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser1(AbstractUser):
    bio = models.CharField(max_length=250)
    username = models.CharField(max_length=50, unique=True, primary_key=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

    def __str__(self):
        return self.username

