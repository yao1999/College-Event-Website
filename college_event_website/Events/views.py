from django.shortcuts import render
from crispy_forms.helper import FormHelper
from .forms import EventForm, CommentForm
import traceback 
from django.http import HttpResponseRedirect, HttpResponse
from .models import Event

# Create your views here.

def event_list(response):
  # return render(response, "Events/base.html")
  events = Event.objects.all()
  print(events)
  return render(response, 'Events/base.html', { 'event_list' : events})

def add_event(response):
  if response.method == "POST":
    if response.POST.get("create-event-btn"):
      event_form = EventForm(response.POST)
      is_private = response.POST.get("universityEvent")
      is_RSO = response.POST.get("rsoEvent")
      if event_form.is_valid():
          event_form.save(is_private, is_RSO)
      return HttpResponseRedirect('../../Events/')
    else:
      return HttpResponseRedirect('../../Events/create')
  event_form = EventForm(None)
  return render(response, "Events/create.html", { 'form' : event_form })

def delete_event(response):
  if response.method == "POST":
    pass
  return render(response, 'Events/?????')

def edit_event(response):
  if response.method == "POST":
    pass
  return render(response, 'Events/?????')

def event_info(response):
  if response.method == "POST":
    comment_form = CommentForm(response.POST)
    if comment_form.is_valid():
        comment_form.save()
    return render(response, 'Events/details.html', { 'form' : comment_form })
  else:
    comment_form = CommentForm(None)
    return render(response, "Events/details.html", { 'form' : comment_form })