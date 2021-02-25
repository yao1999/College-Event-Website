
from django.urls import path
# from .views import (
#   ChooseSignUpView,
#   UserSignUpView,
#   AdminSignUpView,
#   SuperAdminSignUpView
# )
from . import views   # '.' = current directory


urlpatterns = [
   path('register/', views.user_register, name='user_register'),
   path('login/', views.user_login, name='user_login'),
]