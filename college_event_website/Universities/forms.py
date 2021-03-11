from django import forms
from .models import University
from mapbox_location_field.forms import LocationField

def university_directory_path(university_name, instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'university_{0}/{1}'.format(university_name, instance.user.id, filename) 

class UniversityForm(forms.Form):
    name = forms.CharField()
    abbreviation = forms.CharField()
    description = forms.TextField()
    email = forms.CharField()
    location = LocationField(widget=forms.TextInput(attrs={'placeholder': '99.0, 100.1', 'id': 'event_location'}), label="", required=True)
    picture = forms.ImageField() 
    number_of_students = forms.IntegerField()

    def save(self, number_of_students):
        data = self.cleaned_data
        current_university = University(name = data['name'],
                                        abbreviation = data['abbreviation'],
                                        description = data['description'],
                                        email = data['email'],
                                        location = data['location'],
                                        picture = data['picture'],
                                        number_of_students = 0)
        current_university.save()