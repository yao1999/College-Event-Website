from django.db import models

# Create your models here.
MAX_LENGTH_UNIVERSITY_NAME = 100
MAX_LENGTH_UNIVERSITY_ABBREVIATION = 10

def defaultUniversity():
  default = University.objects.first()

  if default is None:
    default = University.objects.create_university(
      name='University of Central Florida',
      abbreviation='UCF'
    )

  return default

class University(models.Model):
  name = models.CharField(max_length = MAX_LENGTH_UNIVERSITY_NAME)
  abbreviation = models.CharField(max_length = MAX_LENGTH_UNIVERSITY_ABBREVIATION)

  def __str__(self): 
    return f'{self.name}'