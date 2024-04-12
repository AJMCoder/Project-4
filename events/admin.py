from django.contrib import admin
from .models import Events, Comment

# Register your models here.
admin.site.register(Events)
admin.site.register(Comment)