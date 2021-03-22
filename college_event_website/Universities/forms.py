from django import forms
from .models import University, Photos
# from mapbox_location_field.forms import LocationField

def university_directory_path(university_name, instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'university_{0}/{1}'.format(university_name, instance.user.id, filename) 

# def find_number_of_students(university_name):
#     current_university = University.objects.filter(name = university_name)
#     if len(current_university) > 0:
#         return current_university.number_of_students
    
#     return 0
# class PhotosForm(forms.Form):
#     photo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)  
#     class Meta:
#         model = Photos
#         fields = ('photo', )


class UniversityForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'University Name', 'class': 'text-center text-white', 'id': 'university_name'}), label="", required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'University Description', 'class': 'text-center text-white', 'id': 'university_description'}), label="", required=True)
    number_of_students = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '99', 'id': 'university_student_number', 'class': 'text-center text-white'}), label="", required=True)

    def save(self, latitude, longitude, university_photos):
        data = self.cleaned_data
        current_university = University(name = data['name'],
                                        description = data['description'],
                                        number_of_students = data['number_of_students'],
                                        latitude = latitude, 
                                        longitude = longitude)
                                        
        current_university.save()
        for photo in university_photos:
            current_university.pictures.add(photo)
            current_university.save()
        current_university.save()