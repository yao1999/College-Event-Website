from django.shortcuts import render
from rest_framework import generics
from .models import User
# from .forms import RegisterUser
from django.http import HttpResponse, HttpResponseRedirect


def user_register(response):
  if response.method == "POST":
    if response.POST.get("UserRegisterButton"):
      first_name = response.POST.get("UserFirstName")
      last_name = response.POST.get("UserLastName") 
      email = response.POST.get("UserEmail")
      username = response.POST.get("UserUsername")
      password = response.POST.get("UserPassword")

      current_user = User(
        first_name = first_name,
        last_name = last_name,
        email = email,
        username = username,
        password = password,
        is_admin = False,
        is_super_admin = False
      )
      current_user.save()
      # print(first_name)
      # print(last_name)
      # print(email)
      # print(username)
      # print(password)
      

          
    # elif response.POST.get()
    # form = RegisterUser(response.POST)
    # if form.is_valid() == True:
      # current_user = User(
      #   username = form.cleaned_data["username"],
      #   password = form.cleaned_data["password"],
      #   email = form.cleaned_data["email"]
      #   )

  return render(response, "Users/register.html") 

