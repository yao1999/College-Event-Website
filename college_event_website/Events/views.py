from django.shortcuts import render
from crispy_forms.helper import FormHelper
from .forms import CreateEventForm
import traceback 
from django.http import HttpResponseRedirect, HttpResponse
from .models import Event

# Create your views here.

def event(response):
  try:
    return render(response, "Events/base.html")
  except: 
    # printing stack trace 
    traceback.print_exc()


def add_event(response):
  try:
    # model = Event
    if response.method == "POST":
      if response.POST.get("create-event-btn"):
        event_form = CreateEventForm(response.POST)
        is_private = response.POST.get("universityEvent")
        is_RSO = response.POST.get("rsoEvent")
        if event_form.is_valid():
            event_form.save(is_private, is_RSO)
        return HttpResponseRedirect('../../Events/')
      else:
        return HttpResponseRedirect('../../Events/create')
    else:
      event_form = CreateEventForm(None)
      return render(response, "Events/create.html", { 'form' : event_form })
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