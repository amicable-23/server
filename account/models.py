from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

# Create your models here.

class user(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="profile", null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    
    USERNAME_FIELD = "email"
    
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    objects = CustomUserManager()
