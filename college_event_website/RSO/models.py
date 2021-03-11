from django.db import models
from Users.models import User

# Create your models here.
class Rso(models.Model):
  name = models.CharField(max_length = 255, null=False)
  students = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students')
  admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')

  def __str__(self):
    return self.name
