
from django.urls import path
# from .views import (
#   ChooseSignUpView,
#   UserSignUpView,
#   AdminSignUpView,
#   SuperAdminSignUpView
# )
from .views import UserView
# from . import views   # '.' = current directory

urlpatterns = [
   path('', UserView.as_view(), name='register')
]