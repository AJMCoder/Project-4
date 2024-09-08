from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views import generic 
from django.contrib import messages
from django.views.generic import DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Event, Comment
from .forms import CommentForm, EventForm

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('event_detail', slug=event.slug)
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

# Create your views here.
class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1)
    template_name = "events/events.html"
    context_object_name = "events"
    paginate_by = 6

def event_list(request):
    events = Event.objects.filter(status=1)
    return render(request, 'events/events.html', {'events': events})

class EventDetail(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

    def get_object(self):
        return get_object_or_404(Event, slug=self.kwargs['slug'])
    
# Allow users to update their own events.
class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('events')

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super().get_object(queryset=queryset)
        if not obj.author == self.request.user:
            raise PermissionDenied()
        return obj


# Allow users to delete their own events.
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super().get_object(queryset=queryset)
        if not obj.author == self.request.user:
            raise PermissionDenied()
        return obj

    def get_success_url(self):
        return reverse_lazy('event_detail', kwargs={'slug': self.object.slug})
    


def event_detail(request, slug):
    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, slug=slug)
    comments = event.comments.filter(approved=True).order_by('-created_at')
    comment_count = comments.count()
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.event = event
            new_comment.author = request.user
            new_comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            comment_form = CommentForm()  # Reinitialize the form after saving

    context = {
        'event': event,
        'comments': comments,
        'comment_count': comment_count,
        'comment_form': comment_form,
    }
    return render(request, 'events/event_detail.html', context)