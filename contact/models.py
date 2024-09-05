from django.db import models

# Create your models here.

class Contact(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"New message from {self.fname} {self.lname}: {self.body} at {self.created}"