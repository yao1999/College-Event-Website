from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from .forms import RsoForm
from django.http import HttpResponseRedirect, HttpResponse
from Users.models import User
from .models import Rso
from Universities.models import University
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/Users/login/')
def list_rsos(response):
    if response.method == 'POST':
        if response.POST.get("search-button"):
            rsos = search_rso_by_name(response)
            if rsos is None:
                rsos = search_rso_by_university(response)
    else:
        rsos = Rso.objects.all().order_by('id')
    all_university = University.objects.all()
    return render(response, 'RSO/base.html', {
      'rsos': rsos,
      'all_university': all_university
    })

@login_required(login_url='/Users/login/')
def add_rso(response):
    if response.method == 'POST':
        students = get_emails(response)
        
        if check_university(response, students) == True:
            RSOForm = RsoForm(response.POST)
            if RSOForm.is_valid():
                RSOForm.save(students)
                messages.success(response, "RSO added")
        return HttpResponseRedirect('../../RSO/')
    else:
        RSOForm = RsoForm(None)
        return render(response, "RSO/create.html", {
            'form': RSOForm
        })

@login_required(login_url='/Users/login/')
def rso_info(response, rso_id):
    rso = Rso.objects.filter(id = rso_id).first()
    if response.method == 'POST':
        if response.POST.get("join-rso-btn"):
            student = User.objects.filter(id = response.user.id).first()
            if student is not None:
                rso.students.add(student)
                messages.success(response, "User joined the Rso")
            return HttpResponseRedirect('../../RSO/')
    if rso is None:
        messages.warning(response, "RSO does not exist")
        return HttpResponseRedirect('../../RSO/')
    return render(response, 'RSO/details.html',{
        'rso': rso
    })
  

def delete_rso():
    pass

def edit_rso():
    pass

def check_user(email, is_admin=False):
    current_user = User.objects.filter(email=email, is_admin=is_admin).first()
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

def check_university(response, students):
    university_name = response.POST.get("universityname")

    for student in students:
        if student.university.name is not university_name:
            return False

    return True

def get_emails(response):
    student_emails = get_emails(response)
    students = []
    for student_email in student_emails:
        is_in_db, current_student = check_user(student_email)
        if is_in_db is True:
            students.append(current_student)
    return students

def search_rso_by_name(response):
    rso_name =response.POST.get("RsoName")
    rsos = Rso.objects.filter(name = rso_name)

    if len(rsos) > 0:
        return rsos
    
    return None

def search_rso_by_university(response):
    university_name = response.POST.get("search-university")
    university = University.objects.filter(name = university_name).first()

    if university is None:
        rsos = Rso.objects.all().order_by('id')
        return rsos
    
    rsos = Rso.objects.filter(university = university)


    return university