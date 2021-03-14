from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from .forms import RsoForm
from django.http import HttpResponseRedirect, HttpResponse
from Users.models import User
from .models import Rso
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/Users/login/')
def list_rsos(response):
    if response.method == 'POST':
        if response.POST.get("search-button"):
            rso_name =response.POST.get("RsoName")
            rsos = Rso.objects.filter(name = rso_name)
            return render(response, 'RSO/base.html', {
                'rsos': rsos
            })
        else:
            return HttpResponseRedirect('../../RSO/')
    rsos = Rso.objects.all().order_by('id')
    return render(response, 'RSO/base.html', {
      'rsos': rsos
    })

@login_required(login_url='/Users/login/')
def add_rso(response):
    if response.method == 'POST':
        student_emails = get_emails(response)
        students = []
        for student_email in student_emails:
            is_in_db, current_student = check_user(student_email)
            print(current_student.username)
            if is_in_db is True:
                students.append(current_student)
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
    return render(response, 'RSO/details.html')
  

def delete_rso():
    pass

def edit_rso():
    pass

def check_user(email, is_admin=False):
    current_user = User.objects.filter(email=email, is_admin=is_admin)
    if len(current_user) > 0:
        return True, current_user[0]
    
    return False, None

def get_emails(response):
    student_emails = []
    total_emails = response.POST.get("number_emails")
    for i in range(1, int(total_emails)+1):
        html_tag = "rso_email_" + str(i) + ""
        if response.POST.get(html_tag) is not None:
            student_emails.append(response.POST.get(html_tag))
    return student_emails