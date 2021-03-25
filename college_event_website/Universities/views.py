from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from .forms import UniversityForm, LocationForm
from django.http import HttpResponseRedirect, HttpResponse
from Users.models import User
from .models import University, Photos, Locations
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.core.files.storage import FileSystemStorage

@login_required(login_url='/Users/login/')
def list_universities(response):
  if response.method == "POST":
    if response.POST.get("search-button"):
      university_name =response.POST.get("UniversityName")
      universities = University.objects.filter(name = university_name)
      return render(response, 'Universities/base.html', {
        'universities': universities
      })
    else:
      return HttpResponseRedirect('../../Universities/')
  else:
    universities = University.objects.all().order_by('id')
    return render(response, 'Universities/base.html', {
      'universities': universities
    })

@login_required(login_url='/Users/login/')
def add_university(response):
  if response.user.is_super_admin is False:
    messages.error(response, "Not super admin")
    return HttpResponseRedirect('../../Universities/')
  else:
    if response.method == "POST":
      if response.POST.get("create-university-btn"):
        university_form = UniversityForm(response.POST)
        if university_form.is_valid():
            location = get_location(response)
            university_photos = get_photos(response, university_form.data['name'])
            university_form.save(location, university_photos)
            messages.success(response, "University added")
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
  current_university = University.objects.filter(id = university_id)
  if len(current_university) <= 0:
    return HttpResponseRedirect('../../Universities/')
  else:
    current_university = current_university[0]
    if response.method == "POST":
      if response.POST.get("join-university-btn"):
        current_user = User.objects.filter(id = response.user.id).update(university = current_university)
        return HttpResponseRedirect('../../Universities/')
    else:
      return render(response, "Universities/details.html", {
        "University_Name": current_university.name,
        "num_of_students": current_university.number_of_students,
        "Description": current_university.description
      })
  


def delete_university():
    pass

def edit_university():
    pass


def get_photos(request, university_name):
  photos = []
  total_photos = request.POST.get("number_photos")
  folder='Universities/images/' + str(university_name) + '/' 
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
  