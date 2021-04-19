
from django.urls import path
from . import views   # '.' = current directory


urlpatterns = [
   path('register/', views.user_register, name='user_register'),
   path('login/', views.user_login, name='user_login'),
   path('logout/', views.user_logout, name='user_logout'),
   path('profile', views.profile, name='profile'),
   ]