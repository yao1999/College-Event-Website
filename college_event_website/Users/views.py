from django.shortcuts import render, redirect
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer