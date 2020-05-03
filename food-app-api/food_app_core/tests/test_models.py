from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    
    def test_registration_is_successfull(self):
        email = 'adam.peter@test.com'
        password = 'TestPass123'
        firstname = 'adam'
        lastname = 'peter'
        user = get_user_model().objects.create_user(
            firstname,
            lastname,
            email,
            password
        )
        self.assertEqual(user.Email,email)
        self.assertTrue(user.check_password(password))


    def test_on_empty_email_address_registration_failed(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                'adam',
                'john',
                Email = None,
                password = '123444'
            )
    
            
    def test_create_superuser(self):
        email = 'adam.peter@test.com'
        password = 'TestPass123'
        firstname = 'adam'
        lastname = 'peter'
        user = get_user_model().objects.create_superuser(          
            Email = email,
            password =password,
             firstname = firstname,
            lastname = lastname,
        )
        self.assertTrue(user.is_superuser)