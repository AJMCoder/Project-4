from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fname', 'lname', 'email', 'body']

        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'email': 'Email',
            'body': 'Message',
        }