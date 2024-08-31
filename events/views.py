from django.shortcuts import render, get_object_or_404
from django.views import generic 
from django.contrib import messages
from django.views.generic import DetailView
from .models import Event, Comment
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