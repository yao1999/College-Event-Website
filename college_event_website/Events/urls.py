from django.urls import path
from . import views


urlpatterns = [
   path('create', views.add_event, name='add_event'),
   path('', views.event, name = 'event')
]