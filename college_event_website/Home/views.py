from django.shortcuts import render

# Create your views here.
  
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
def home(request):
  return HttpResponseRedirect("../../Users/login")