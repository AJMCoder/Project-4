from django.shortcuts import render
from django.views import generic
from .models import Event

# Create your views here.
class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1)
    template_name = "events/index.html"
    context_object_name = "events"
    paginate_by = 6

