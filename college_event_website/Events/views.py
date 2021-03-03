from django.shortcuts import render
from crispy_forms.helper import FormHelper
from .forms import EventForm, CommentForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import Event, Comment
from Users.models import User
from django.contrib import messages

# Create your views here.

def list_events(response):
  # return render(response, "Events/base.html")
  events = Event.objects.all()
  # print(events)
  return render(response, 'Events/base.html', { 'event_list' : events})

def add_event(response):
  if response.method == "POST":
    if response.POST.get("create-event-btn"):
      event_form = EventForm(response.POST)
      is_private = response.POST.get("universityEvent")
      is_RSO = response.POST.get("rsoEvent")
      if event_form.is_valid():
          event_form.save(is_private, is_RSO)
          messages.success(response, "Event added")
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

def event_info(response, event_id):
  if response.method == "POST":
    comment_form = CommentForm(response.POST)
    if comment_form.is_valid():
        current_event = Event.objects.filter(id = event_id)[0]
        current_user = User.objects.filter(id = response.user.id)[0]
        comment_form.save(current_user, current_event)
        messages.success(response, "Comment added")
    return HttpResponseRedirect('../../Events/' + str(event_id) + '')
  else:
    comment_form = CommentForm(None)
    try:
      event = Event.objects.filter(id = event_id)[0]
    except:
      messages.error(response, "Event Not Found")
      return HttpResponseRedirect('../../Events/')
    all_comments = Comment.objects.filter(event= event)
    rating  = get_rating(all_comments)
    return render(response, "Events/details.html", { 
      'form' : comment_form,
      'event' : event,
      'rating': rating,
      'comments': all_comments
      })


def get_rating(all_comments):
  if len(all_comments) == 0:
    return 0
  
  count = 0
  for comment in all_comments:
    count += comment.rating 

  result =  count / len(all_comments)

  return round(result, 2)
