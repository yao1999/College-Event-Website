from django.db import models
from location_field.models.plain import PlainLocationField


# Create your models here.

# this is the path for image store
# instance	An instance of the model where the ImageField is defined. More specifically,
#           this is a particular instance where the current file is being attached.
# filename	The filename that was originally given to the file. 
#           This may or may not be taken into account when determining the final destination path
def university_directory_path(university_name, instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'university_{0}/{1}'.format(university_name, instance.user.id, filename) 

class University(models.Model):
  name = models.CharField(max_length = 100, null=False)
  abbreviation = models.CharField(max_length = 10, null=False)
  description = models.TextField()
  email = models.CharField(max_length = 254, null=False)
  location = PlainLocationField(based_fields= ['city'], zoom= 7)
  picture = models.ImageField(upload_to = university_directory_path) 
  number_of_students = models.IntegerField()

  def __str__(self): 
    return f'{self.name}'