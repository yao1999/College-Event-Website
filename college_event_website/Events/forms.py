from django import forms
from .models import Event, Comment

RATINGS = (
    ('', 'Rate...'),
    ('1', '1 Star'),
    ('2', '2 Stars'),
    ('3', '3 Stars'),
    ('4', '4 Stars'),
    ('5', '5 Stars')
)

class EventForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Event Name', 'class': 'text-center text-white', 'id': 'event_name'}), label="", required=True)
    date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'bg-transparent', 'id': 'event_date'}), label="", required=True)
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '10:00', 'id': 'event_start'}), label="", required=True)
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '12:00', 'id': 'event_end'}), label="", required=True)
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '99.0, 100.1', 'id': 'event_location'}), label="", required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Describe the event.', 'class': 'text-center text-white', 'id': 'event_description'}), label="", required=True)
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '8881239999', 'id': 'event_phone', 'class': 'text-center text-white'}), label="", required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'email@realemails.com', 'id': 'event_email', 'class': 'text-center text-white'}), label="", required=True)
    
    # need to add is_RSO , is_private, and so on
    def save(self, is_private, is_RSO):
        data = self.cleaned_data
        current_event = Event(name = data['name'], 
                              date = data['date'],
                              start_time = data['start_time'], 
                              end_time = data['end_time'],
                              location = data['location'],
                              description = data['description'],
                              phone = data['phone'],
                              email = data['email'],
                              is_public = True if (is_RSO == None and is_private == None) else False,
                              is_RSO = True if is_RSO else False,
                              is_private = True if is_private else False)
        current_event.save()


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comment Here', 'class': 'text-center text-white', 'id': 'create_event_comment'}), label="", required=True)
    rating = forms.ChoiceField(choices=RATINGS)

    def save(self):
        data = self.cleaned_data
        current_comment = Comment(
            content = data['content'],
            rating = data['rating']
        )
        current_comment.save()