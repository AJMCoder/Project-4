from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

class ContactView(View):
    def get(self, request, *args, **kwargs):
        """Return data"""
        return render(
            request,
            'contact.html',
            {
                'contact_form': ContactForm()
            }
        )

    def post(self, request, *args, **kwargs):
        """Send data"""
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Thank you for your message! We will get back to you soon.')

        else:
            contact_form = ContactForm()
        return render(
            request,
            'contact.html',
            {
                'contact_form': ContactForm()
            }
        )

