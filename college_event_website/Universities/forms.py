from django import forms
from .models import University, Locations


class UniversityForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'University Name', 'class': 'text-center text-white', 'id': 'university_name'}), label="", required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'University Description', 'class': 'text-center text-white', 'id': 'university_description'}), label="", required=True)
    number_of_students = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '99', 'id': 'university_student_number', 'class': 'text-center text-white'}), label="", required=True)

    def save(self, location, university_photos, super_admin):
        data = self.cleaned_data
        current_university = University(name = data['name'],
                                        description = data['description'],
                                        number_of_students = data['number_of_students'],
                                        super_admin = super_admin,
                                        location = location)
                                        
        current_university.save()
        for photo in university_photos:
            current_university.pictures.add(photo)
            current_university.save()
        current_university.save()

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