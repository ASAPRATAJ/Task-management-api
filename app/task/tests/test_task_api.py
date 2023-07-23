"""
Tests for the task API.
"""
import datetime

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import Task, User

TASKS_URL = reverse(r'task:task-list')
TASK_CREATE_URL = reverse(r'task:task-create')


# CREATE_TASK_URL = reverse('task:task-create')


class TaskAPITest(TestCase):
    """Test task API requests."""

    def setUp(self):
        self.client = APIClient()
        self.office = User.objects.create(name='Office')
        self.production = User.objects.create(name='Production')
        self.date = datetime.date.today().day

    def test_retrieve_tasks(self):
        Task.objects.create(
            task_name='Test task',
            description='This is test task',
            created_by=self.office,
        )
        Task.objects.create(
            task_name='Test task2',
            description='This is test task',
            created_by=self.office,
            assigned_to=self.production,
        )

        response = self.client.get(TASKS_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_task(self):
        payload = {
            'task_name': 'Test task',
            'description': 'This is a test task',
            'created_by': self.office.id,
            'assigned_to': self.production.id,
        }

        response = self.client.post(TASK_CREATE_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().task_name, 'Test task')
