from django.shortcuts import render
from crispy_forms.helper import FormHelper
from .forms import EventForm, CommentForm, LocationForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import Event, Comment, Locations
from Universities.models import University
from Users.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from RSO.models import Rso

# Create your views here.

@login_required(login_url='/Users/login/')
def list_events(response):
  if response.method == "POST":
    if response.POST.get("search-button"):
      is_location, location_info = search_by_location(response)
      university = search_by_university_name(response)
      if is_location is False:
        if university is not None:
          events = Event.objects.filter(university = university)
        else:
          events = []
      else:
        if university is not None:
          events = Event.objects.filter(location = location_info, university = university)
        else:
          events = Event.objects.filter(location = location_info)
  else:
    events = Event.objects.filter(is_approved = True)
  
  user_university = University.objects.filter(name = response.user.university).first()
  return render(response, 'Events/base.html', { 
    'events' : events,
    'user_university': user_university
    })

@login_required(login_url='/Users/login/')
def add_event(response):
  if response.user.is_admin is False:
    messages.error(response, "Only RSO admins can make events")
    return HttpResponseRedirect('../../Events/')
  else:
    if response.method == "POST":
      if response.POST.get("create-event-btn"):
        event_form = EventForm(response.POST)
        if response.user.is_admin == False:
          messages.warning(response, "User is not admin")
          return HttpResponseRedirect('../../Events/create')
        if check_timestamp(event_form.data['start_time'], event_form.data['end_time']) == False:
          messages.warning(response, "End time is earlier than start time")
          return HttpResponseRedirect('../../Events/create')
        is_private = response.POST.get("universityEvent")
        is_RSO = None
        user_university = None
        user_rso = None 
        if event_form.is_valid():
            location = get_location(response)
            if response.POST.get("universityEvent"):
              user_university = response.user.university
            if response.POST.get("rsoEvent"):
              is_RSO = response.POST.get("rsoEvent")
              user_rso = get_rso(response.user)
            event_form.save(is_private, is_RSO, location, user_university, user_rso, response.user)
            messages.success(response, "Event added")
        return HttpResponseRedirect('../../Events/')
      else:
        return HttpResponseRedirect('../../Events/create')
    event_form = EventForm(None)
    location_form = LocationForm(None)
    return render(response, "Events/create.html", { 
      'form' : event_form,
      'location_form': location_form
    })


def edit_event(response):
  if response.method == "POST":
    pass
  return render(response, 'Events/?????')


@login_required(login_url='/Users/login/')
def event_info(response, event_id):
  if response.method == "POST":
    if response.POST.get("delete-comment-btn"):
      comment_id = response.POST.get("delete-comment-btn")
      delete_comment(comment_id, response.user)
      return HttpResponseRedirect('../../Events/' + str(event_id) + '')
    
    if response.POST.get("edit-comment-btn"):
      comment_id = response.POST.get("edit-comment-btn")
      comment_rating = response.POST.get("edit-comment-btn")
      if delete_comment(comment_id, response.user) == False:
        return  HttpResponseRedirect('../../Events/' + str(event_id) + '')

    comment_form = CommentForm(response.POST)
    if comment_form.is_valid():
        current_event = Event.objects.filter(id = event_id).first()
        current_user = User.objects.filter(id = response.user.id).first()
        comment_form.save(current_user, current_event)
        messages.success(response, "Comment added")
    return HttpResponseRedirect('../../Events/' + str(event_id) + '')
  else:
    comment_form = CommentForm(None)
    event = Event.objects.filter(id = event_id).first()
    all_comments = Comment.objects.filter(event= event).order_by('-timestamp')
    rating  = get_rating(all_comments)
    return render(response, "Events/details.html", { 
      'form' : comment_form,
      'event' : event,
      'rating': rating,
      'comments': all_comments,
      'longitude': event.location.longitude,
      'latitude': event.location.latitude,
      })

@login_required(login_url='/Users/login/')
def approve(response):
  if response.method == "POST":
    disapprove = response.POST.get("DisapproveButton")
    approve = response.POST.get("ApproveButton")

    if approve:
      current_event = Event.objects.filter(id = approve).first()
      current_event.is_approved = True
      current_event.save()
    elif disapprove:
      current_event = Event.objects.filter(id = disapprove).delete()

  events = Event.objects.filter(is_approved = False)
  return render(response, "Events/approve.html", {
    'events': events
  })

def delete_comment(comment_id, current_user):
  current_comment = Comment.objects.filter(id=comment_id)[0]
  if current_comment.user.id == current_user.id:
    current_comment.delete()
    return True
  else:
    return False

def get_rating(all_comments):
  if len(all_comments) == 0:
    return 0
  
  count = 0
  for comment in all_comments:
    count += comment.rating 

  result =  count / len(all_comments)

  return round(result, 2)

def is_in_db(latitude, longitude, location_in_db):
  if len(location_in_db) < 0:
    return None
  
  for location in location_in_db:
    if (location.latitude == latitude and location.longitude == longitude):
      return location
  
  return None

def get_location(response):
  location_name = response.POST.get("location_name"),
  latitude = response.POST.get("latitude"),
  longitude = response.POST.get("longitude")

  if isinstance(location_name, str) is False:
    location_name = location_name[0]

  if isinstance(latitude, str) is False:
    latitude = latitude[0]
  
  if isinstance(longitude, str) is False:
    longitude = longitude[0]

  location_in_db = Locations.objects.filter(location_name=location_name)

  current_location = is_in_db(latitude, longitude, location_in_db)

  if current_location is None:
    location_form = LocationForm(response.POST)
    if location_form.is_valid():
      current_location = location_form.save()
          
  return current_location

def search_by_university_name(response):
  university_name = response.POST.get("search-university")
  university = University.objects.filter(name = university_name).first()

  if university is None:
    return None

  return university


def search_by_location(response):
  location = response.POST.get("search-form-location-name")
  latitude = response.POST.get("search-form-latitude")
  longitude = response.POST.get("search-form-longitude")

  current_location = Locations.objects.filter(location_name = location).first()

  if current_location is not None:
    return True, current_location
  
  current_location = Locations.objects.filter(latitude = latitude, longitude = longitude).first()

  if current_location is not None:
    return True, current_location

  return False, None


def get_rso(user):
    all_rso = Rso.objects.all()

    for rso in all_rso:
      if rso.students.filter(id=user.id).exists():
        return rso
    
    return None
  
def check_timestamp(start_time, end_time):
  print(start_time)
  print(end_time)

  if start_time < end_time:
    return False
  
  return True