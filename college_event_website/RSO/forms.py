from django import forms
from .models import Rso
from Users.models import User, RsoNumber
from Universities.models import University


class RsoForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'RSO Name', 'class': 'text-center text-white', 'id': 'rso_name'}), label="", required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'RSO Description', 'class': 'text-center text-white', 'id': 'rso_description'}), label="", required=True)
    admin_email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Administrator Email*', 'class': 'text-center text-white', 'id': 'rso_admin_email'}), label="", required=True)

    def save(self, students, university_name):
        data = self.cleaned_data
        current_admin = User.objects.filter(email = data['admin_email'], is_admin = True).first()
        if current_admin is not None:
            current_university = find_university(current_admin, students, university_name)
            if current_university is not None: 
                total_students = int(1 + len(students))
                current_rso = Rso(name = data['name'], 
                                  description = data['description'],
                                  university = current_university,
                                  admin = current_admin,
                                  total_students = total_students,
                                  status = True if total_students >= 5 else False)
                current_rso.save()
                current_RsoNumber = RsoNumber(username = current_admin.username, rso=current_rso.id)
                current_RsoNumber.save()
                current_rso.admin.rsos.add(current_RsoNumber)
                for student in students:
                    current_RsoNumber = RsoNumber(username = student.username, rso=current_rso.id)
                    current_RsoNumber.save()
                    student.rsos.add(current_RsoNumber)
                    current_rso.students.add(student)
                    current_rso.save()
                current_rso.save()

def find_university(admin, students, university_name):
    current_university = University.objects.filter(name = university_name).first()

    if check_university_for_members(students, admin, current_university) is True:
        return current_university
    
    return None
    

def check_university_for_members(students, admin, current_university):
    if admin.university.name != current_university.name:
        return False
    for student in students:
        admin_email_domain = admin.email.split('@')[1]
        student_email_domain = student.email.split('@')[1]
        if (admin_email_domain != student_email_domain and 
            admin.university.name != student.university.name):
            return False

    return True
