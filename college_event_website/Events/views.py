from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def event(request):
  return render(request, 'Events/base.html')