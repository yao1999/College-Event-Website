from django.db import models
from django.urls import reverse 
from datetime import date, time
from location_field.models.plain import PlainLocationField
# from address.models import AddressField
from Users.models import User

DEFAULT_DATE = date(2000, 1, 1)
DEFAULT_START_TIME = time(12, 0)
DEFAULT_END_TIME = time(13, 0)

# Create your models here.
class Event(models.Model):
  id = models.AutoField(primary_key=True) 
  name = models.CharField(max_length = 150)
  description = models.TextField()
  date = models.DateField(default=DEFAULT_DATE)
  startTime = models.TimeField(default=DEFAULT_START_TIME)
  endTime = models.TimeField(default=DEFAULT_END_TIME)
  location = PlainLocationField(based_fields=['city'], zoom=7)
  isApproved = models.BooleanField(default=False)
  isPrivate = models.BooleanField(default=False) 
  isRSO = models.BooleanField(default=False)

  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  def __str__(self):
    return self.name

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  event = models.ForeignKey(Event, on_delete=models.CASCADE) 

#   def save_model(self, request, obj, form, change):
#     if obj.user == defaultUser: 
#       obj.user = request.user 
  
  def __str__(self):
    return f'{self.event.name} {self.user.username}'