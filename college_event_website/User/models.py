from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from University.models import University

# Create your models here.

def defaultUser():
    default = User.objects.first()

    if default is None:
        default = User.objects.create_user(
          username='defaultUser1',
          email='COP4710@gmail.com', 
          password='123456',
          is_admin=False,
          is_super_admin=False
          )

    return default

# AbstractUser include Username, first_name,last_name, email, 
# date_joined and so on, and I just extend 
# https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/models/
class User(AbstractUser):
  is_admin = models.BooleanField(default=False, null=False) 
  is_super_admin = models.BooleanField(default=False, null=False)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.png', upload_to='profile_pics')

  def __str__(self):
    return f'{self.user.username} Profile'

  def is_this_user_admin(self):
    return self.is_admin
  
  def is_this_user_super_admin(self):
    return self.is_super_admin

  def save(self, **kwargs):
    super().save()

    image = Image.open(self.image.path) 

    if image.width > 300 or image.height > 300:
      output_size = (300, 300) 
      image.thumbnail(output_size)
      image.save(self.image.path)
  
class UniversityList(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE) 
  universities = models.ManyToManyField(University, default=defaultUser)

  def __str__(self):
    return f'{self.owner.username} UnivList'
  
  @classmethod 
  def add_university(cls, user, new_university):
    # Grabs the university list who's owner is me
    universityList, created = cls.objects.get_or_create(user = user)
    universityList.universities.add(new_university)

  @classmethod 
  def remove_university(cls, user, new_university):
    universityList, created = cls.objects.get_or_create(user = user)
    universityList.universities.remove(new_university)
