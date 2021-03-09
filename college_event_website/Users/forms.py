from django import forms
from .models import User
from Universities.models import University


class UserForm(forms.Form):
    pass

    def save(self, is_super_admin):
        data = self.cleaned_data
        current_user = User(first_name = data["first_name"],
                            last_name = data["last_name"],
                            email = data["email"],
                            username = data["username"],
                            password = data["password"],
                            is_admin = False,
                            is_super_admin = True if is_super_admin else False,
                            university = find_university())
        current_user.save()
    
    def find_university(self):
        email = self.cleaned_data["email"]
        domains = email.split('@')[1].split('.') # knights.ucf.edu, we can just get the [1], but I just get all in case
        all_universities = University.objects.all()

        for university in all_universities:
            if domains.count(university.abbreviation):
                return university.name

        return None