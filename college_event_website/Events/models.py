from django.db import models
from django.urls import reverse 
from datetime import datetime, date, time
from location_field.models.plain import PlainLocationField
from phone_field import PhoneField
# from address.models import AddressField
from Users.models import User

# DEFAULT_DATE = date(2000, 1, 1)
# DEFAULT_START_TIME = time(12, 0)
# DEFAULT_END_TIME = time(13, 0)

# Create your models here.
class Event(models.Model):
  id = models.AutoField(primary_key=True) 
  name = models.CharField(max_length = 150, null=False)
  description = models.TextField()
  date = models.DateField(default=date.today, null=False)
  start_time = models.TimeField(null=False)
  end_time = models.TimeField(null=False)
  location = PlainLocationField(based_fields=['city'], zoom=7, null=False)
  phone = PhoneField(blank=True, help_text='Contact phone number', null=False)
  email = models.CharField(max_length = 254, null=False)
  is_approved = models.BooleanField(default=False)
  is_public = models.BooleanField(default=False) 
  is_private = models.BooleanField(default=False) 
  is_RSO = models.BooleanField(default=False)

  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  
  def __str__(self):
    return self.name

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  rating = models.IntegerField()
  timestamp = models.TimeField(default=datetime.now().strftime("%H:%M:%S"), null=False)

  event = models.ForeignKey(Event, on_delete=models.CASCADE) 

#   def save_model(self, request, obj, form, change):
#     if obj.user == defaultUser: 
#       obj.user = request.user 
  
  def __str__(self):
    return f'{self.event.name} {self.user.username}'