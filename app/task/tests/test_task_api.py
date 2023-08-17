"""
Tests for the task API.
"""
import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import Task
from task.serializers import TaskDetailSerializer

TASKS_URL = reverse(r'task:task-list')
TASK_CREATE_URL = reverse(r'task:task-create')


def task_detail_url(task_id):
    detail = reverse('task:task-detail', args=[task_id])
    return detail


def create_task(**params):
    payload = {
        'task_name': 'Test task',
        'description': 'This is test task',
    }
    payload.update(params)

    task = Task.objects.create(**params)
    return task


class TaskAPITest(TestCase):
    """Test task API requests."""

    def setUp(self):
        self.client = APIClient()
        self.office = get_user_model().objects.create_user(
            name='Office',
            email='office@example.com',
            password='testpass123',
        )
        self.production = get_user_model().objects.create_user(
            name='Production',
            email='production@example.com',
            password='testpass123',
        )
        self.date = datetime.date.today().day

    def test_list_tasks(self):
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

    def test_retrieve_task_detail(self):
        task = create_task(created_by=self.office, assigned_to=self.production)

        url = task_detail_url(task.id)
        response = self.client.get(url)

        serializer = TaskDetailSerializer(task)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
