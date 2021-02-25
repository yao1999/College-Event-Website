from django.shortcuts import render, redirect
from rest_framework import generics
from .models import User
from django.http import HttpResponseRedirect
# from .forms import RegisterUser

def user_register(response):
  if response.method == "POST":
    if response.POST.get("UserRegisterButton") or response.POST.get("SuperUserRegisterButton"):

      first_name = response.POST.get("UserFirstName")
      last_name = response.POST.get("UserLastName") 
      email = response.POST.get("UserEmail")
      username = response.POST.get("UserUsername")
      password = response.POST.get("UserPassword")
      
      is_super_admin = False
      if response.POST.get("SuperUserRegisterButton"):
        is_super_admin = True

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
      return HttpResponseRedirect('../../Users/login')

    else:
      return HttpResponseRedirect('../../Users/register')
     

  return render(response, "Users/register.html") 


def user_login(response):
  if response.method == "POST":
    if response.POST.get("UserLoginButton") or response.POST.get("SuperUserLoginButton"):
      username = response.POST.get("UserUsername")
      password = response.POST.get("UserPassword")

      if response.POST.get("UserLoginButton"):
        current_user = User.objects.get(username = username, is_super_admin = False)
      else:
        current_user = User.objects.get(username = username, is_super_admin = True)
      
      if current_user.password == password:
        return redirect('home')

      else:
        return HttpResponseRedirect('../../Users/register')

    else:
      return HttpResponseRedirect('../../Users/login')

  return render(response, "Users/login.html") 