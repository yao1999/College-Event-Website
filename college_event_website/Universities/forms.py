from django import forms
from .models import University, Photos


class UniversityForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'University Name', 'class': 'text-center text-white', 'id': 'university_name'}), label="", required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'University Description', 'class': 'text-center text-white', 'id': 'university_description'}), label="", required=True)
    number_of_students = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '99', 'id': 'university_student_number', 'class': 'text-center text-white'}), label="", required=True)

    def save(self, location, university_photos):
        data = self.cleaned_data
        current_university = University(name = data['name'],
                                        description = data['description'],
                                        number_of_students = data['number_of_students'],
                                        location = location)
                                        
        current_university.save()
        for photo in university_photos:
            current_university.pictures.add(photo)
            current_university.save()
        current_university.save()