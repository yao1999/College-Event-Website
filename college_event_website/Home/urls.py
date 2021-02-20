from django.urls import path

from . import views   # '.' = current directory

urlpatterns = [
  path('', views.home, name='home'),
]