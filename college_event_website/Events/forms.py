from django import forms
from .models import Event, Comment, Locations
from RSO.models import Rso
RATINGS = (
    ('1', '1 Star'),
    ('2', '2 Stars'),
    ('3', '3 Stars'),
    ('4', '4 Stars'),
    ('5', '5 Stars')
)

class EventForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Event Name*', 'class': 'text-center text-white', 'id': 'event_name'}), label="", required=True)
    category = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Event Category*', 'class': 'text-center text-white', 'id': 'event_category'}), label="", required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Describe the event.*', 'class': 'text-center text-white', 'id': 'event_description'}), label="", required=True)
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '10:00*', 'id': 'event_start*'}), label="", required=True)
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '12:00*', 'id': 'event_end*'}), label="", required=True)
    date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'bg-transparent', 'id': 'event_date*'}), label="", required=True)
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '8881239999*', 'id': 'event_phone*', 'class': 'text-center text-white'}), label="", required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'email@realemails.com*', 'id': 'event_email*', 'class': 'text-center text-white'}), label="", required=True)

    # need to add is_RSO , is_private, and so on
    def save(self, is_private, is_RSO, location, user_university, user_rso, current_user):
        data = self.cleaned_data
        current_rso = Rso.objects.filter(id=user_rso.id).first() if user_rso is not None else None
        current_event = Event(name = data['name'], 
                              date = data['date'],
                              start_time = data['start_time'],
                              category = data['category'],
                              end_time = data['end_time'],
                              description = data['description'],
                              phone = data['phone'],
                              email = data['email'],
                              is_public = True if (is_RSO == False and is_private == None) else False,
                              is_RSO = True if is_RSO else False,
                              is_private = True if is_private else False,
                              is_approved = False if is_RSO == False else True,
                              location = location,
                              university = user_university,
                              rso = current_rso if current_rso is not None else None,
                              admin = current_user)
        current_event.save()


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comment Here', 'class': 'text-center text-white', 'id': 'create_event_comment'}), label="", required=True)
    rating = forms.ChoiceField(choices=RATINGS, label="", required=True)

    def save(self, current_user, current_event):
        data = self.cleaned_data
        current_comment = Comment(content = data['content'],
                                  rating = data['rating'],
                                  user = current_user,
                                  event = current_event)
        current_comment.save()

class LocationForm(forms.Form):
    location_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Location Name*', 'class': 'text-center text-white', 'id': 'location_name'}), label="", required=True)
    latitude = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Latitude*', 'class': 'text-center text-white', 'id': 'location_latitude'}), label="", required=True)
    longitude = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Longitude*', 'class': 'text-center text-white', 'id': 'location_longitude'}), label="", required=True)

    def save(self):
        data = self.cleaned_data
        current_location = Locations(location_name = data['location_name'],
                                    latitude = data['latitude'],
                                    longitude = data['longitude'])
        current_location.save()
        return current_location