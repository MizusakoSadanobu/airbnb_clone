from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AccountsTests(TestCase):
    def test_register_view(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Register')

    def test_login_view(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login')

    def test_register_user(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
            'user_type': 'guest'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertEqual(User.objects.count(), 1)

    def test_login_user(self):
        User.objects.create_user(username='testuser', password='12345')
        response = self.client.post(reverse('accounts:login'), {
            'username': 'testuser',
            'password': '12345'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
