from django import forms
from .models import Event

class CreateEventForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Event Name'}))
    date = forms.DateField(widget=forms.SelectDateWidget())
    start_time = forms.TimeField(widget=forms.TimeField())
    end_time = forms.TimeField(widget=forms.TimeField())
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '99.0, 100.1'}))
    university_event = forms.CheckboxInput()
    rso_event = forms.CheckboxInput()
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Describe the event.'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '888-888-8888'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'email@realemails.com'}))

