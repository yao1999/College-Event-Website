from django import forms
from .models import Event

class CreateEventForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Event Name', 'class': 'text-center text-white', 'id': 'event_name'}), label="")
    date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'bg-transparent', 'id': 'event_date'}), label="")
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '10:00', 'id': 'event_start'}), label="")
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '12:00', 'id': 'event_end'}), label="")
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '99.0, 100.1', 'id': 'event_location'}), label="")
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Describe the event.', 'class': 'text-center text-white', 'id': 'event_description'}), label="")
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '8881239999', 'id': 'event_phone', 'class': 'text-center text-white'}), label="")
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'email@realemails.com', 'id': 'event_email', 'class': 'text-center text-white'}), label="")