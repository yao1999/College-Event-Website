from django.shortcuts import render
from .forms import CreateEventForm
# from django.contrib.auth.decorators import login_required
import traceback 
# Create your views here.

def event(response):
  try:
    return render(response, 'Events/base.html')
  except: 
    # printing stack trace 
    traceback.print_exc()


def add_event(response):
  try:
    Eventform = CreateEventForm(response.POST or None)
    if response.method == "POST" and Eventform.is_valid():
      Eventform.save()
      return render(response, 'Events/create.html', {
        'form' : Eventform
        })
    else:
      return render(response, 'Events/create.html', {
        'form' : Eventform
        })
  except: 
    # printing stack trace 
    traceback.print_exc()

def delete_event(response):
  try:
    if response.method == "POST":
      pass
    return render(response, 'Events/?????')
  except: 
    # printing stack trace 
    traceback.print_exc()

def edit_event(response):
  try:
    if response.method == "POST":
      pass
    return render(response, 'Events/?????')
  except: 
    # printing stack trace 
    traceback.print_exc()

def event_info(response):
  try:
    if response.method == "POST":
      pass
    return render(response, 'Events/?????')
  except: 
    # printing stack trace 
    traceback.print_exc()