from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import traceback 
# Create your views here.

def event(request):
  try:
    return render(request, 'Events/base.html')
  except: 
    # printing stack trace 
    traceback.print_exc()