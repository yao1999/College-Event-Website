from django.shortcuts import render, redirect
from .forms import UniversityForm, LocationForm
from django.http import HttpResponseRedirect, HttpResponse
from Users.models import User
from .models import University, Photos, Locations
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.core.files.storage import FileSystemStorage

@login_required(login_url='/Users/login/')
def list_universities(response):
  if response.method == "POST":
    if response.POST.get("search-button"):
      universities = search_university_by_name(response)
      if universities is None:
        universities = search_university_by_location(response)
  else:
    universities = University.objects.all().order_by('id')
  return render(response, 'Universities/base.html', {
    'universities': universities
  })

@login_required(login_url='/Users/login/')
def add_university(response):
  if response.user.is_super_admin is False:
    return HttpResponseRedirect('../../Universities/')
  else:
    if response.method == "POST":
      if response.POST.get("create-university-btn"):
        university_form = UniversityForm(response.POST)
        if university_form.is_valid():
            location = get_location(response)
            university_photos = get_photos(response, university_form.data['name'])
            super_admin = response.user.id
            university_form.save(location, university_photos, super_admin)
        return HttpResponseRedirect('../../Universities/')
      else:
        return HttpResponseRedirect('../../Universities/create')
    else:
      universityForm = UniversityForm(None)
      location_form = LocationForm(None)
      return render(response, "Universities/create.html", {
          'form': universityForm,
          'location_form': location_form
        })

@login_required(login_url='/Users/login/')
def university_info(response, university_id):
  current_university = University.objects.filter(id = university_id).first()
  isInUniveristy = current_university == response.user.university
  isAdmin = ()
  if current_university is None:
    return HttpResponseRedirect('../../Universities/')
  else:
    if response.method == "POST":
      if response.POST.get("join-university-btn"):
        join_or_leave(response.user.id, current_university, is_join=True)
      elif response.POST.get("leave-university-btn"):
        join_or_leave(response.user.id, current_university, is_leave=True)
      elif response.POST.get("delete-university-btn"):
          current_university.delete()
      return HttpResponseRedirect('../../Universities/')
    else:
      all_picture = Photos.objects.filter(university_name = current_university.name)
      return render(response, "Universities/details.html", {
        "University_Name": current_university.name,
        "num_of_students": current_university.number_of_students,
        "Description": current_university.description,
        'longitude': current_university.location.longitude,
        'latitude': current_university.location.latitude,
        'location_name': current_university.location.location_name,
        'isInUniveristy': isInUniveristy,
        'University_Name_For_Photo': current_university.name.replace(' ', ''),
        'all_picture': all_picture
      })


def get_photos(request, university_name):
  photos = []
  total_photos = request.POST.get("number_photos")
  university_name_for_photo = university_name.replace(" ", "")
  folder='Universities/static/Universities/images/' + str(university_name_for_photo) + '/' 
  for i in range(1, int(total_photos)+1):
      html_tag = 'university_photo_' + str(i)
      myfile = request.FILES[html_tag]
      if myfile is not None:
        current_photos = Photos(university_name = university_name, photo_path = myfile.name)
        current_photos.save()
        photos.append(current_photos)
        fs = FileSystemStorage(location=folder)
        filename = fs.save(myfile.name, myfile)
        file_url = fs.url(filename)

  return photos

def is_in_db(latitude, longitude, location_in_db):
  if len(location_in_db) < 0:
    return None
  
  for location in location_in_db:
    if (location.latitude == latitude and location.longitude == longitude):
      return location
  
  return None

def get_location(response):
  location_name = response.POST.get("location_name"),
  latitude = response.POST.get("latitude"),
  longitude = response.POST.get("longitude")

  location_in_db = Locations.objects.filter(location_name=location_name)

  current_location = is_in_db(latitude, longitude, location_in_db)

  if current_location is None:
    location_form = LocationForm(response.POST)
    if location_form.is_valid():
      current_location = location_form.save()
  return current_location

def search_university_by_name(response):
  university_name = response.POST.get("search-form-university-name")
  universities = University.objects.filter(name = university_name)

  if len(universities) > 0:
    return universities
  
  return None

def search_university_by_location(response):
  location = response.POST.get("search-form-location-name")
  latitude = response.POST.get("search-form-latitude")
  longitude = response.POST.get("search-form-longitude")

  current_location = Locations.objects.filter(location_name = location).first()

  if current_location is not None:
    universities = University.objects.filter(location = current_location)
    return universities
  
  current_location = Locations.objects.filter(latitude = latitude, longitude = longitude).first()

  if current_location is not None:
    universities = University.objects.filter(location = current_location)
    return universities

  return []

def join_or_leave(user_id, university, is_join=False, is_leave=False):
    student = User.objects.filter(id = user_id)
    if len(student) == 1:
        if is_join is True:
            student.update(university = university)
        if is_leave is True:
            student.update(university = None)
        return True
    
    return False