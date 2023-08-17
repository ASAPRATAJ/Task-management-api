from rest_framework import serializers
from core.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the task object."""

    class Meta:
        model = Task
        fields = ['task_name', 'created_by', 'assigned_to', 'is_completed', 'created_at']


class TaskDetailSerializer(TaskSerializer):

    class Meta(TaskSerializer.Meta):
        model = Task
        fields = TaskSerializer.Meta.fields + ['description']
