from django.shortcuts import render, redirect
from rest_framework import generics
from .models import User
from django.http import HttpResponseRedirect
import traceback 
from django.contrib.auth import login, logout

def user_register(response):
  try:
    if response.method == "POST":
      if response.POST.get("UserRegisterButton") or response.POST.get("SuperUserRegisterButton"):

        current_user = User(
            first_name = response.POST.get("UserFirstName"),
            last_name = response.POST.get("UserLastName"),
            email = response.POST.get("UserEmail"),
            username = response.POST.get("UserUsername"),
            password = response.POST.get("UserPassword"),
            is_admin = False,
            is_super_admin = True if response.POST.get("SuperUserRegisterButton") else False
          )
        current_user.save()
        return HttpResponseRedirect('../../Users/login')

      else:
        return HttpResponseRedirect('../../Users/register')
      
    return render(response, "Users/register.html") 
  except: 
    # printing stack trace 
    traceback.print_exc() 


def user_login(response):
  try:
    if response.method == "POST":
      if response.POST.get("UserLoginButton") or response.POST.get("SuperUserLoginButton"):
        username = response.POST.get("UserUsername")
        password = response.POST.get("UserPassword")

        current_user = ""
        try:
          if response.POST.get("UserLoginButton"):
            current_user = User.objects.get(username = username, is_super_admin = False)
          elif response.POST.get("SuperUserLoginButton"):
            current_user = User.objects.get(username = username, is_super_admin = True)
        except:
          pass
        
        if current_user != "":
          if current_user.password == password:
            login(response, current_user)
            return HttpResponseRedirect('../../Events/')
          else:
            return HttpResponseRedirect('../../Users/login')

      else:
        return HttpResponseRedirect('../../Users/login')

    return render(response, "Users/login.html") 
  except: 
    # printing stack trace 
    traceback.print_exc()
  
def user_logout(response):
  logout(response)
  return HttpResponseRedirect("../../")

def auto_login_for_coder(response):
  try:
    username = "testForCoder"
    is_admin = True
    is_super_admin = True
    try:
      current_user = User.objects.get(username = username, is_admin = is_admin, is_super_admin = is_super_admin)
      login(response, current_user)
    except: 
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
    return HttpResponseRedirect("../../Events/create")
  except: 
    # printing stack trace 
    traceback.print_exc()