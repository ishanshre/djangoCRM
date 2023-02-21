"""Testing admin site"""

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class AdminSiteTest(TestCase):
    """Testing admin sites"""
    def setUp(self):
        """Initializing test variables"""
        self.client = Client() # client that acts as client for testing

        """
        Creating a super user
        using client to login admin site with superuser admin_user 
        """
        self.admin_user = User.objects.create_superuser(
            email="admin123@admin.com",
            username="admin123",
            password="hello@123"
        )
        self.client.force_login(self.admin_user)

        self.user = User.objects.create_user(
            email="user@user.com",
            username="user",
            password="hello@123"
        )

    def test_user_list_works(self):
        """Testing admin stie user list works"""
        url=reverse("admin:accounts_user_changelist")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200) # CHECKS if we get proper url
        self.assertContains(res, self.user.username)
        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.is_staff)
    
    def test_user_edit_page_loads(self):
        """Testing user change page loads"""
        url = reverse("admin:accounts_user_change", args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
    
    def test_user_add_works(self):
        """Test user add loads"""
        url = reverse("admin:accounts_user_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)