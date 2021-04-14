from django.db import models
from django.contrib.auth.models import AbstractUser
from Universities.models import University
from django.db.models import ManyToManyField

# Create your models here.

class RsoNumber(models.Model):
  username = models.CharField(max_length=100, null=False)
  rso = models.IntegerField()

  def __str__(self):
    return self.username

class User(AbstractUser):
  password = models.CharField(max_length=500, null=False)
  is_admin = models.BooleanField(default=False) 
  is_super_admin = models.BooleanField(default=False)
  university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)
  rsos = ManyToManyField(RsoNumber)
  

  def __str__(self):
    return self.username
