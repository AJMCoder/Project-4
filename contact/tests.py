# contact/tests.py
from django.test import TestCase
from .forms import ContactForm

class ContactFormTest(TestCase):

    def test_contact_form_valid_data(self):
        form = ContactForm(data={
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john.doe@example.com',
            'body': 'This is a test message.',
        })

        self.assertTrue(form.is_valid())

    def test_contact_form_invalid_data(self):
        form = ContactForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    def test_contact_form_partial_data(self):
        form = ContactForm(data={
            'fname': 'John',
            'lname': '',
            'email': 'john.doe@example.com',
            'body': '',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('lname', form.errors)
        self.assertIn('body', form.errors)