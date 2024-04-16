from django.shortcuts import render, get_object_or_404
from django.views import generic 
from django.views.generic import DetailView
from .models import Event

# Create your views here.
class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1)
    template_name = "events/index.html"
    context_object_name = "events"
    paginate_by = 6

class EventDetail(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

    def get_object(self):
        return get_object_or_404(Event, slug=self.kwargs['slug'])
