"""
Views for task API.
"""
from rest_framework import status, viewsets

from core.models import Task
from task.serializers import TaskSerializer, TaskDetailSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskDetailSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        return self.queryset.order_by('-id')

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskSerializer

        return self.serializer_class

