
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status as HttpStatus

CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    return get_user_model().objects.create_user(params)

class PublicUserApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_user_is_success(self):
        payload = {
	            "FirstName":"testuser",
	            "LastName":"user",
	            "Email":"testuser@gmail.com",
	            "password":"test123"	
            }
        res = self.client.post(CREATE_USER_URL,payload,"json")
        self.assertEqual(res.status_code,HttpStatus.HTTP_201_CREATED)
