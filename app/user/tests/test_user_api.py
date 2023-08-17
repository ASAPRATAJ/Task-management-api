"""
Tests for the User API.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import User

CREATE_USER_URL = reverse('user:create')
LIST_USER_URL = reverse('user:list')


def create_user(**params):
    user = get_user_model().objects.create_user(**params)
    return user


class TestPublicUserAPI(TestCase):
    """Test for the unauthenticated User"""
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        payload = {
            'email': 'test@example.com',
            'name': 'Test name',
            'password': 'testpass123',
        }

        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], payload['email'])

    def test_retrieve_list_of_users(self):
        create_user(
            email='test@example.com',
            name='User one',
            password='testpass123',
        )
        create_user(
            email='test2@example.com',
            name='User two',
            password='testpass123',
        )

        response = self.client.get(LIST_USER_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestAuthenticatedUserAPI(TestCase):
    """Tests for the authenticated User"""
    def setUp(self):
        self.user = create_user(
            email='test@example.com',
            name='TestName'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    # def test_get_user_detail(self):
    #     
