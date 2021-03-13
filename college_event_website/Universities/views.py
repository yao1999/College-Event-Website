from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from .forms import UniversityForm
from django.http import HttpResponseRedirect, HttpResponse
from Users.models import User
from .models import University
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
            university_form.save()
            messages.success(response, "University added")
        return HttpResponseRedirect('../../Universities/')
      else:
        return HttpResponseRedirect('../../Universities/create')
    else:
      universityForm = UniversityForm(None)
      return render(response, "Universities/create.html", {
          'form': universityForm,
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
        "location": current_university.location,
        "num_of_students": current_university.number_of_students,
        "Description": current_university.description
      })
  


def delete_university():
    pass

def edit_university():
    pass