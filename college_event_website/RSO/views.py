from django.shortcuts import render, redirect
from .forms import RsoForm
from django.http import HttpResponseRedirect, HttpResponse
from Users.models import User, RsoNumber
from .models import Rso
from Universities.models import University
from django.contrib.auth.decorators import login_required

@login_required(login_url='/Users/login/')
def list_rsos(response):
    if response.method == 'POST':
        if response.POST.get("search-button"):
            rsos = search_rso_by_name(response)
            if rsos is None:
                rsos = search_rso_by_university(response)
    else:
        rsos = Rso.objects.filter(status=True).order_by('id')
        
    user_university = University.objects.filter(name = response.user.university).first()
    return render(response, 'RSO/base.html', {
      'rsos': rsos,
      'user_university': user_university
    })

@login_required(login_url='/Users/login/')
def rso_inactive_info(response):
    inactive_rsos = Rso.objects.filter(status=False).order_by('id')
    return render(response, 'RSO/inactiveRsos.html', {
      'rsos': inactive_rsos
    })

@login_required(login_url='/Users/login/')
def add_rso(response):
    if response.method == 'POST':
        students = get_students(response)
        RSOForm = RsoForm(response.POST)
        university_name = response.POST.get("pick-university")

        if (check_university(students, university_name) == True and 
            check_admin(RSOForm.data['admin_email'], university_name) == True):
            if RSOForm.is_valid():
                sign_admin(RSOForm.data['admin_email'])
                RSOForm.save(students, university_name)
        return HttpResponseRedirect('../../RSO/')
    else:
        RSOForm = RsoForm(None)
        all_university = University.objects.all().order_by('id')
        user_university = University.objects.filter(name = response.user.university).first()
        return render(response, "RSO/create.html", {
            'form': RSOForm,
            'all_university': all_university,
            'user_university': user_university
        })

@login_required(login_url='/Users/login/')
def rso_info(response, rso_id):
    rso = Rso.objects.filter(id = rso_id).first()
    isInRSO = rso.students.filter(id=response.user.id).exists()
    isSameUniversity = (rso.university == response.user.university) 
    if isInRSO is False:
        isInRSO = True if rso.admin.id == response.user.id else False
    if response.method == 'POST':
        if response.POST.get("join-rso-btn"):
            join_or_leave(response.user.id, rso, is_join=True)
        elif response.POST.get("leave-rso-btn"):
            join_or_leave(response.user.id, rso, is_leave=True)
        elif response.POST.get("delete-rso-btn"):
            rso.delete()
            response.user.is_admin = False
            response.user.save()
        return HttpResponseRedirect('../../RSO/')
    if rso is None:
        return HttpResponseRedirect('../../RSO/')
    return render(response, 'RSO/details.html',{
        'rso': rso,
        'isInRSO': isInRSO,
        'same_university': isSameUniversity
    })

def check_user(email):
    current_user = User.objects.filter(email=email).first()
    if current_user is not None:
        return True, current_user
    
    return False, None

def get_emails(response):
    student_emails = []
    total_emails = response.POST.get("number_emails")
    for i in range(1, int(total_emails)+1):
        html_tag = "rso_email_" + str(i) + ""
        if response.POST.get(html_tag) is not None:
            student_emails.append(response.POST.get(html_tag))
    return student_emails

def check_university(students, university_name):

    for student in students:
        if student.university.name != university_name:
            return False

    return True

def check_admin(admin_email, university_name):
    admin = User.objects.filter(email=admin_email).first()

    if admin is None:
        return False
    
    if university_name != admin.university.name:
        return False

    return True


def get_students(response):
    student_emails = get_emails(response)
    students = []
    for student_email in student_emails:
        is_in_db, current_student = check_user(student_email)
        if is_in_db is True:
            students.append(current_student)
    return students

def search_rso_by_name(response):
    rso_name =response.POST.get("RsoName")
    rsos = Rso.objects.filter(name = rso_name, status =True)

    if len(rsos) > 0:
        return rsos
    
    return None

def search_rso_by_university(response):
    university_name = response.POST.get("search-university")
    university = University.objects.filter(name = university_name).first()

    if university is None:
        rsos = Rso.objects.filter(status = True).order_by('id')
        return rsos
    
    rsos = Rso.objects.filter(university = university, status = True).order_by('id')
    return rsos

def join_or_leave(user_id, rso, is_join=False, is_leave=False):
    student = User.objects.filter(id = user_id).first()
    if student is not None:
        if is_join is True:
            rso.students.add(student)
            rso.total_students = rso.students.count() + 1
            rso.status = False if (rso.total_students < 5) else True
            current_RsoNumber = RsoNumber(
                username = student.username,
                rso = rso.id
            )
            current_RsoNumber.save()
            student.rsos.add(current_RsoNumber)
        if is_leave is True:
            rso.students.remove(student)
            rso.total_students = rso.students.count() + 1
            rso.status = False if (rso.total_students < 5) else True
            current_RsoNumber = RsoNumber.objects.get(username = student.username, rso=rso.id)
            student.rsos.remove(current_RsoNumber)
            
        rso.save()
        student.save()
        print(student.rsos.count())
    

def sign_admin(admin_email):
    current_admin = User.objects.filter(email = admin_email).first()

    if current_admin is not None:
        current_admin.is_admin = True
        current_admin.save()
