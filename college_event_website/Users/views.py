from django.shortcuts import render, redirect
from rest_framework import generics
from .models import User
from django.http import HttpResponseRedirect
import traceback 
from django.contrib.auth import login, logout
from django.contrib import messages
from RSO.models import Rso
from cryptography.fernet import Fernet


def user_register(response):
  if response.user.is_authenticated is True:
    messages.error(response, "User Authorized Already")
    return HttpResponseRedirect('../../Events/')
  else:
    if response.method == "POST":
      if response.POST.get("UserRegisterButton"):
        user_check_and_register(response, "user")

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
        if current_user is not None:
          login(response, current_user)
          messages.success(response, "Welcome!!!")
          return HttpResponseRedirect('../../Users/profile')
        else:
          messages.warning(response, "Password incorrect")
          return HttpResponseRedirect('../../Users/login')
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

  password = encrypt_password(password) 
  current_user = User(
    first_name = first_name,
    last_name = last_name,
    email = email,
    username = username,
    password = password,
    is_admin = False,
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
    current_user_password = decrypt_password(current_user.password)
    if current_user_password == password:
      return current_user
  
  return None


def auto_login_for_coder(response):
  current_user = User.objects.get(username = "Zefeng")
  login(response, current_user)
  return HttpResponseRedirect("../../Users/profile")


def get_rso(user):
    all_rso = Rso.objects.all()

    rsos = []

    for rso in all_rso:
      if rso.students.filter(id=user.id).exists():
        rsos.append(rso)
      elif rso.admin.id == user.id:
        rsos.append(rso)
    
    return rsos

def encrypt_password(password):
  key = b'HkLYcD5m5zH9VYNEQt9GpWzxq87SHHbhpxvFR9LgF9Q=' # this is bytes
  fernet = Fernet(key)
  enc_password = fernet.encrypt(password.encode()).decode()
  return enc_password


def decrypt_password(password_in_db):
  key = b'HkLYcD5m5zH9VYNEQt9GpWzxq87SHHbhpxvFR9LgF9Q=' # this is bytes
  fernet = Fernet(key)
  dec_password = fernet.decrypt(str.encode(password_in_db)).decode()
  return dec_password

# ------------------------------------------------------------------------------------------
# real data
# 10 uses, 5 RSOs, 20 events, 10 comments

def insert_users(name, is_super_admin):
  first_name = name.split(" ")[0]
  last_name = name.split(" ")[1]
  username = name.split(" ")[0]
  password = "123asd"
  password = encrypt_password(password)
  email = first_name + "." + last_name + "@gmail.com"

  current_user = User(
    first_name = first_name,
    last_name = last_name,
    email = email,
    username = username,
    password = password,
    is_admin = False,
    is_super_admin = is_super_admin
  )
  current_user.save()

def ten_users(response):
  names = ["Oliver Ward",
        "Ryan Kelly",
        "Luke Patel",
        "Hayden Cole",
        "Frederick Booth",
        "Mason Hendrix",
        "Crew Bell",
        "Zander Gilbert",
        "Camdyn Daniel",
        "Maurice Haynes",]
  is_admin = False
  is_super_admin = False

  for name in names:
      insert_users(name, is_super_admin)
  
  return HttpResponseRedirect("../../")

def three_super_admins(response):
  names = ["Zefeng Yao",
          "Alexandra French",
          "Jialin Zheng",]
  is_admin = False
  is_super_admin = True

  for name in names:
      insert_users(name, is_super_admin)

  return HttpResponseRedirect("../../")
