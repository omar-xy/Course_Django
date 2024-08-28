from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class ola(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    password='ola' 

