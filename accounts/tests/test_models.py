"""
Testing the database models for custom user model
"""


from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class ModelTests(TestCase):
    def setUp(self):
        """Initializing test variables"""
        self.username = "test"
        self.email = "email@emal.com"
        self.password="hello@123"
    
    """Testing Database Model: custom user model"""
    def test_create_user(self):
        """Testing Creating a new user"""
        user = User.objects.create_user(
            email=self.email,
            username=self.username,
            password=self.password
        )
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        """Testing creating new superuser"""
        superUser = User.objects.create_superuser(
            email=self.email,
            username=self.username,
            password=self.password
        )
        self.assertEqual(superUser.email, self.email)
        self.assertEqual(superUser.username, self.username)
        self.assertTrue(superUser.check_password(self.password))
        self.assertTrue(superUser.is_active)
        self.assertTrue(superUser.is_staff)
        self.assertTrue(superUser.is_superuser)
    
    def test_user_created_with_no_username_raise_value_error(self):
        """Testing value raised when creating user with no username"""
        with self.assertRaises(ValueError):
            User.objects.create_user(username="",email=self.email, password=self.password)

    def test_superuser_created_with_no_username_raise_value_error(self):
        """Testing value raised when creating superuser with no username"""
        with self.assertRaises(ValueError):
            User.objects.create_superuser(username="", email=self.email, password=self.password)
