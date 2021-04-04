from django.db import models
from django.db.models import ManyToManyField


# Create your models here.

# this is the path for image store
# instance	An instance of the model where the ImageField is defined. More specifically,
#           this is a particular instance where the current file is being attached.
# filename	The filename that was originally given to the file. 
#           This may or may not be taken into account when determining the final destination path

class Photos(models.Model):
  university_name = models.CharField(max_length = 100, null=False)
  photo_path = models.CharField(max_length = 100, null=False)

  def __str__(self):
    return self.university_name


class Locations(models.Model):
  location_name = models.CharField(max_length = 100, null=False)
  latitude = models.CharField(max_length = 100, null=False)
  longitude = models.CharField(max_length = 100, null=False)

  def __str__(self):
    return self.location_name


class University(models.Model):
  name = models.CharField(max_length = 100, null=False)
  super_admin = models.IntegerField(null=True)
  description = models.TextField()
  location = models.ForeignKey(Locations, on_delete=models.CASCADE) 
  pictures = ManyToManyField(Photos)
  number_of_students = models.IntegerField()

  def __str__(self): 
    return self.name