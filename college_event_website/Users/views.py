from django.shortcuts import render, redirect
from rest_framework import generics
from .models import User
from django.http import HttpResponseRedirect
import traceback 
from django.contrib.auth import login, logout
from django.contrib import messages
from RSO.models import Rso

def user_register(response):
  if response.user.is_authenticated is True:
    messages.error(response, "User Authorized Already")
    return HttpResponseRedirect('../../Events/')
  else:
    if response.method == "POST":
      if response.POST.get("UserRegisterButton"):
        user_check_and_register(response, "user")

      elif response.POST.get("AdminRegisterButton"):
        user_check_and_register(response, "admin")

      elif response.POST.get("SuperUserRegisterButton"):
        user_check_and_register(response, "faculty")

      return HttpResponseRedirect('../../Users/login')
    else:
      return render(response, "Users/register.html") 


def user_login(response):
  if response.user.is_authenticated is True:
      messages.error(response, "User Authorized Already")
      return HttpResponseRedirect('../../Events/')
  else:
    if response.method == "POST":
      if response.POST.get("UserLoginButton"):
        current_user = user_check_and_login(response, "user")
      elif response.POST.get("SuperUserLoginButton"):
        current_user = user_check_and_login(response, "faculty")
        if current_user is not None:
            login(response, current_user)
            messages.success(response, "Welcome!!!")
            return HttpResponseRedirect('../../Users/profile')
        else:
          messages.warning(response, "Password incorrect")
          return HttpResponseRedirect('../../Users/login')

      else:
        return HttpResponseRedirect('../../Users/login')

    else:
      return render(response, "Users/login.html") 
  
def user_logout(response):
  logout(response)
  return HttpResponseRedirect("../../")

def profile(response):
  users_rsos = get_rso(response.user)
  return render(response, 'Users/profile.html', {
    'users_rsos': users_rsos,
    'haveRSO': True if len(users_rsos) > 0 else False,
  })

def user_check_and_register(response, user_type):
  first_name = response.POST.get(user_type + "FirstName")
  last_name = response.POST.get(user_type + "LastName")
  email = response.POST.get(user_type + "Email")
  username = response.POST.get(user_type + "Username")
  password = response.POST.get(user_type + "Password")
  current_user = User(
    first_name = first_name,
    last_name = last_name,
    email = email,
    username = username,
    password = password,
    is_admin = True if user_type == "admin" else False,
    is_super_admin = True if user_type == "faculty" else False
  )
  current_user.save()

def user_check_and_login(response, user_type):
  username = response.POST.get(user_type + "Username")
  password = response.POST.get(user_type + "Password")

  current_user = None
  if user_type == "user":
    current_user = User.objects.filter(username = username, is_super_admin = False).first()
  elif user_type == "faculty":
    current_user = User.objects.filter(username = username, is_super_admin = True).first()
  
  if current_user is not None:
    if current_user.password == password:
      return current_user
  
  return None


def auto_login_for_coder(response):
  username = "testForCoder"
  is_admin = True
  is_super_admin = True
  try:
    current_user = User.objects.get(username = username)
    login(response, current_user)
  except Exception: 
    current_user = User(
      first_name = username,
      last_name = "Yao",
      email = "testForCoder@gmail.com",
      username = username,
      password = "1234asd",
      is_admin = is_admin,
      is_super_admin = is_super_admin
    )
    current_user.save()
    login(response, current_user)
  return HttpResponseRedirect("../../Users/profile")


def get_rso(user):
    all_rso = Rso.objects.all()

    rsos = []

    for rso in all_rso:
      if rso.students.filter(id=user.id).exists():
        rsos.append(rso)
        
    
    return rsos