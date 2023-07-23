"""
Views for task API.
"""
from rest_framework import status, viewsets

from core.models import Task
from task.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        return self.queryset.order_by('-id')