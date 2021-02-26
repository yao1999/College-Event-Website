from django.urls import path
# from .views import (
#   ChooseSignUpView,
#   UserSignUpView,
#   AdminSignUpView,
#   SuperAdminSignUpView
# )
from . import views   # '.' = current directory


urlpatterns = [
   path('', views.event, name='event'),
]