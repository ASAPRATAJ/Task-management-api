from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = User
        fields = '__all__'
