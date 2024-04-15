from django.contrib import admin
from .models import Event, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', 'created_at')
    search_fields = ['title', 'description',]
    list_filter = ('status', 'created_at')
    summernote_fields = ('description',)
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Comment)
