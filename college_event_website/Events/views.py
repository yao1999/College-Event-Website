from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
import traceback 
# Create your views here.

def event(response):
  try:
    return render(response, "Events/base.html")
  except: 
    # printing stack trace 
    traceback.print_exc()


def add_event(response):
  try:
    if response.method == "POST":
      pass
    return render(response, 'Events/?????')
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