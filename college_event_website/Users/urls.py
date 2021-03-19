
from django.urls import path
from . import views   # '.' = current directory


urlpatterns = [
   path('register/', views.user_register, name='user_register'),
   path('login/', views.user_login, name='user_login'),
   path('auto-login/', views.auto_login_for_coder, name='auto_login_for_coder'), # need to delete before submit
   path('logout/', views.user_logout, name='user_logout'),
   path('profile', views.profile, name='profile')
]