from django import forms
from .models import Rso


class RsoForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'RSO Name', 'class': 'text-center text-white', 'id': 'rso_name'}), label="", required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'RSO Description', 'class': 'text-center text-white', 'id': 'rso_description'}), label="", required=True)
    # university = 
    # number_of_students = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '99', 'id': 'rso_student_number', 'class': 'text-center text-white'}), label="", required=True)
    admin_email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Administrator Email*', 'class': 'text-center text-white', 'id': 'rso_admin_email'}), label="", required=True)

    def save(self, students, admin):
        data = self.cleaned_data
        current_rso = Rso(name = data['name'],
                          students = students, 
                          admin = admin)
        current_rso.save()