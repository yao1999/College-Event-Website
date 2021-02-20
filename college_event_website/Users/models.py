from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  is_admin = models.BooleanField(default=False, null=False) 
  is_super_admin = models.BooleanField(default=False, null=False)

  def __str__(self):
    return self.username 

  def is_this_user_admin(self):
    return self.is_admin
  
  def is_this_user_super_admin(self):
    return self.is_super_admin