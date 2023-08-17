"""
Views for User API.
"""
from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ListUserView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
