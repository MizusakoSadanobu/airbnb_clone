from django.test import TestCase
from django.urls import reverse
from .models import Listing
from django.contrib.auth.models import User

class ListingTests(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Create a listing
        self.listing = Listing.objects.create(
            title='Test Listing',
            description='This is a test description.',
            price=100.0,
            image_url='http://example.com/image.jpg'
        )

    def test_listing_list_view(self):
        response = self.client.get(reverse('listing_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Listing')

    def test_add_listing_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('add_listing'), {
            'title': 'Another Listing',
            'description': 'Another description',
            'price': 200.0,
            'image_url': 'http://example.com/another.jpg'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertEqual(Listing.objects.count(), 2)

    def test_listing_model(self):
        self.assertEqual(str(self.listing), 'Test Listing')
