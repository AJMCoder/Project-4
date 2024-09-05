from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    class ContactAdmin(admin.ModelAdmin):

        list_display = ('fname', 'lname', 'email', 'created')
        search_fields = ('fname', 'lname', 'email', 'body')
        list_filter = ('fname', 'lname', 'email')