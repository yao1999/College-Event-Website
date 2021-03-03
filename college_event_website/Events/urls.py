from django.urls import path
from . import views


urlpatterns = [
   path('create', views.add_event, name='add_event'),
   path('', views.list_events, name = 'list_events'),
   path('details', views.event_info, name='event_info')
]