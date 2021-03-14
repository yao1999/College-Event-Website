from django.urls import path
from . import views


urlpatterns = [
   path('create', views.add_university, name='add_university'),
   path('', views.list_universities, name = 'list_universities'),
   # path('details', views.university_info, name='university_info')
   path('<int:university_id>', views.university_info, name='university_info')
]