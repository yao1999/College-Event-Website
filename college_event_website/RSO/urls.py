from django.urls import path
from . import views


urlpatterns = [
   path('create', views.add_rso, name='add_rso'),
   path('', views.list_rsos, name = 'list_rsos'),
   path('details', views.rso_info, name='rsoy_info')
#    path('<int:university_id>', views.university_info, name='university_info')
]