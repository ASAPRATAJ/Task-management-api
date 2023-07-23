from rest_framework import serializers
from core.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the task object."""

    class Meta:
        model = Task
        fields = '__all__'
