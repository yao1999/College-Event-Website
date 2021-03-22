from django.db import models
from mapbox_location_field.models import LocationField  
from django.db.models import ManyToManyField

ucf_location = [28.6014075,-81.20134150000001]

# Create your models here.

# this is the path for image store
# instance	An instance of the model where the ImageField is defined. More specifically,
#           this is a particular instance where the current file is being attached.
# filename	The filename that was originally given to the file. 
#           This may or may not be taken into account when determining the final destination path
def university_directory_path(university_name, instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'university_{0}/{1}'.format(university_name, filename) 

class Photos(models.Model):
  university_name = models.CharField(max_length = 100, null=True)
  photo_path = models.CharField(max_length = 100, null=True)

  def __str__(self):
    return self

class University(models.Model):
  name = models.CharField(max_length = 100, null=False)
  description = models.TextField()
  latitude = models.CharField(max_length = 100, null=True)
  longitude = models.CharField(max_length = 100, null=True)
  pictures = ManyToManyField(Photos)
  number_of_students = models.IntegerField()

  def __str__(self): 
    return self.name