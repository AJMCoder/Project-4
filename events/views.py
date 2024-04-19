from django.shortcuts import render, get_object_or_404
from django.views import generic 
from django.contrib import messages
from django.views.generic import DetailView
from .models import Event
from .forms import CommentForm

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

def event_detail(request, slug):
    query = Event.objects.filter(status=1)
    event = get_object_or_404(Event, slug=slug)
    comments = event.comments.all().order_by('-created_at')
    comment_count = comments.count.filter(approved=True).count()
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = event
            new_comment.author = request.user
            new_comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted and awaiting approval'
            )
    comment_form = CommentForm()


    return render(
        request,
        'events/event_detail.html',
        {
            "event": event,
            "comments": comments,
            "author": event.author,
            "comment_count": comment_count,
            "comment_form": comment_form
        },
    )