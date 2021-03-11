from django import forms
from .models import Rso


class RsoForm(forms.Form):
    name = forms.CharField()

    def save(self, students, admin):
        data = self.cleaned_data
        current_rso = Rso(name = data['name'],
                          students = students, 
                          admin = admin)
        current_rso.save()