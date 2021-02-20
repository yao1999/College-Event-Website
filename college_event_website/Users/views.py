from django.shortcuts import render
from rest_framework import generics
from .models import User
from .forms import RegisterUser
from django.http import HttpResponse, HttpResponseRedirect


def user_register(response):
  if response.method == "POST":
    form = RegisterUser(response.POST)
    if form.is_valid() == True:
      current_user = User(
        username = form.cleaned_data["username"],
        password = form.cleaned_data["password"],
        email = form.cleaned_data["email"]
        )
      current_user.save()
      return HttpResponseRedirect("/register")
  else:  
    form = RegisterUser()
  return render(response, "Users/user_register.html", {
    "user_register_form": form
    }) 

