from django.shortcuts import render
from crispy_forms.helper import FormHelper
from .forms import UniversityForm
from django.http import HttpResponseRedirect, HttpResponse
from Users.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/Users/login/')
def list_universities(response):
  # return render(response, "Events/base.html")
#   events = Event.objects.all()
  # print(events)
#   return render(response, 'Events/base.html', { 'events' : events})
    return render(response, 'Universities/base.html')

def add_university(response):
#   if response.method == "POST":
#     if response.POST.get("create-event-btn"):
#       event_form = EventForm(response.POST)
#       is_private = response.POST.get("universityEvent")
#       is_RSO = response.POST.get("rsoEvent")
#       if event_form.is_valid():
#           event_form.save(is_private, is_RSO)
#           messages.success(response, "Event added")
#       return HttpResponseRedirect('../../Events/')
#     else:
#       return HttpResponseRedirect('../../Events/create')
#   event_form = EventForm(None)

    universityForm = UniversityForm()
    return render(response, "Universities/create.html", {
        'form': universityForm,
      })

@login_required(login_url='/Users/login/')
def university_info(response):
    return render(response, "Universities/details.html")


def delete_university():
    pass

def edit_university():
    pass