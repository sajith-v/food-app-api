from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminTest(TestCase):

    def SetUp(self):
        self.Client = Client()
        self.AdminUser = get_user_model().objects.create_superuser(
            firstname = 'adam',
            lastname = 'peter',
            email = 'adam.peter@test.com',
            password = 'TestPass123'
        )
        self.Client.force_login(self.AdminUser)
        self.User = get_user_model().objects.create_user(
            firstname = 'Joy',
            lastname = 'peter',
            email = 'joy.peter@test.com',
            password = 'Pass123'
        )

   