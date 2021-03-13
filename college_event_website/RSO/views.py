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
    rsos = Rso.objects.all().order_by('id')
    return render(response, 'RSO/base.html', {
      'universities': rsos
    })

@login_required(login_url='/Users/login/')
def add_rso(response):
    RSOForm = RsoForm()
    return render(response, "RSO/create.html", {
        'form': RSOForm
    })

@login_required(login_url='/Users/login/')
def rso_info(response):
    return render(response, 'RSO/details.html')
  


def delete_rso():
    pass

def edit_rso():
    pass