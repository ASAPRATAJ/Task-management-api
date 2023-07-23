"""
Views for user API.
"""
from rest_framework import status, viewsets

from core.models import User
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


