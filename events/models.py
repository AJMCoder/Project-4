from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_author")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} | written by {self.author}"
    
    # Created a save method to automatically create a slug for the event
    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        # Ensure the slug is unique
        unique_slug = self.slug
        num = 1
        while Event.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{self.slug}-{num}'
            num += 1
        self.slug = unique_slug
        super().save(*args, **kwargs)

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

    