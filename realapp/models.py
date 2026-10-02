from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Registration(models.Model):
    fname = models.CharField(max_length=100, help_text="enter your first name")
    lname = models.CharField(max_length=100, help_text="enter your last name")
    email = models.EmailField(max_length=100, help_text="enter your email")
    def __str__(self):
        return f"userID {self.id}, {self.fname}, {self.lname}"
class MainPage(models.Model):
    pass