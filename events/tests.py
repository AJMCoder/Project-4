# events/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Event

class EventTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.event = Event.objects.create(
            title='Test Event',
            description='Test Description',
            date='2023-12-31 23:59:59+00:00',  # Use timezone-aware datetime
            location='Test Location',
            author=self.user,
            status=1,
            slug='test-event'
        )

    def test_create_event(self):
        response = self.client.post(reverse('create_event'), {
            'title': 'New Event',
            'description': 'New Description',
            'date': '2023-12-31 23:59:59+00:00',  # Use timezone-aware datetime
            'location': 'New Location',
            'status': 1,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Event.objects.filter(title='New Event').exists())

    def test_edit_event(self):
        response = self.client.post(reverse('event_edit', args=[self.event.pk]), {
            'title': 'Updated Event',
            'description': 'Updated Description',
            'date': '2023-12-31 23:59:59+00:00',  # Use timezone-aware datetime
            'location': 'Updated Location',
            'status': 1,
        })
        self.assertEqual(response.status_code, 302)
        self.event.refresh_from_db()
        self.assertEqual(self.event.title, 'Updated Event')

    def test_delete_event(self):
        response = self.client.post(reverse('event_delete', args=[self.event.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Event.objects.filter(pk=self.event.pk).exists())

    def test_events(self):
        response = self.client.get(reverse('events'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.title)

    def test_event_detail(self):
        response = self.client.get(reverse('event_detail', args=[self.event.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.title)