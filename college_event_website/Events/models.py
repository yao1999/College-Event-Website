from django.db import models
from django.urls import reverse 
from datetime import datetime, date
from phone_field import PhoneField
from Users.models import User
from Universities.models import University
from RSO.models import Rso

# Create your models here.

class Locations(models.Model):
  location_name = models.CharField(max_length = 100, null=False)
  latitude = models.CharField(max_length = 100, null=False)
  longitude = models.CharField(max_length = 100, null=False)

  def __str__(self):
    return self.location_name


class Event(models.Model):
  id = models.AutoField(primary_key=True) 
  name = models.CharField(max_length = 150, null=False)
  category = models.CharField(max_length = 150, null=True)
  description = models.TextField()
  date = models.DateField(default=date.today, null=False)
  start_time = models.TimeField(null=False)
  end_time = models.TimeField(null=False)
  location = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True) 
  phone = PhoneField(blank=True, help_text='Contact phone number', null=False)
  email = models.CharField(max_length = 254, null=False)
  is_public = models.BooleanField(default=False) 
  is_private = models.BooleanField(default=False) 
  is_RSO = models.BooleanField(default=False)
  is_approved = models.BooleanField(default=False)
  university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)
  rso = models.ForeignKey(Rso, on_delete=models.CASCADE, null=True, blank=True)
  admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  
  def __str__(self):
    return self.name

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  rating = models.IntegerField()
  timestamp = models.DateTimeField(default=datetime.now(), null=True)

  event = models.ForeignKey(Event, on_delete=models.CASCADE) 
  
  def __str__(self):
    return f'{self.event.name}'