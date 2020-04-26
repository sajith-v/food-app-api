from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    
    def test_registration_is_successfull(self):
        email = 'adam.peter@test.com'
        password = 'TestPass123'
        firstname = 'adam'
        lastname = 'peter'
        user = get_user_model().objects.create_user(
            firstname = firstname,
            lastname = lastname,
            email = email,
            password =password
        )
        self.assertEqual(user.Email,email)
        self.assertTrue(user.check_password(password))


    def test_on_empty_email_address_registration_failed(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                firstname = 'adam',
                lastname = 'john',
                email = None,
                password = '123444'
            )
    
            
    def test_create_superuser(self):
        email = 'adam.peter@test.com'
        password = 'TestPass123'
        firstname = 'adam'
        lastname = 'peter'
        user = get_user_model().objects.create_superuser(
            firstname = firstname,
            lastname = lastname,
            email = email,
            password =password
        )
        self.assertTrue(user.is_superuser)