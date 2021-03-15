from django import forms
from .models import Rso
from Users.models import User
from Universities.models import University


class RsoForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'RSO Name', 'class': 'text-center text-white', 'id': 'rso_name'}), label="", required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'RSO Description', 'class': 'text-center text-white', 'id': 'rso_description'}), label="", required=True)
    # university = 
    # number_of_students = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '99', 'id': 'rso_student_number', 'class': 'text-center text-white'}), label="", required=True)
    admin_email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Administrator Email*', 'class': 'text-center text-white', 'id': 'rso_admin_email'}), label="", required=True)

    def save(self, students):
        data = self.cleaned_data
        current_admin = User.objects.filter(email = data['admin_email'], is_admin = True).first()
        if current_admin is not None:
            current_university = find_university(current_admin, students)
            if current_university is not None: 
                total_students = int(1 + len(students))
                current_rso = Rso(name = data['name'], 
                                  description = data['description'],
                                  university = current_university,
                                  admin = current_admin,
                                  total_students = total_students)
                current_rso.save()
                for student in students:
                    current_rso.students.add(student)
                    current_rso.save()
                current_rso.save()
            else:
                pass # <-- error message

def find_university(admin, students):
    current_university = University.objects.filter(name = admin.university)
    if len(current_university) > 0:
        current_university = current_university[0]
    if check_university(students, admin) is True:
        return current_university
    
    return None
    

def check_university(students, admin):
    for student in students:
        admin_email_domain = admin.email.split('@')[1]
        student_email_domain = student.email.split('@')[1]
        if admin_email_domain != student_email_domain:
            return False

    return True
