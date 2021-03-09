from django.db import models
from django.contrib.auth.models import AbstractUser
from Universities.models import University

# Create your models here.
class User(AbstractUser):
  is_admin = models.BooleanField(default=False) 
  is_super_admin = models.BooleanField(default=False)
  university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)

  def __str__(self):
    return self.username 