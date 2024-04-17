from django.contrib import admin
from .models import Rule
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Rule)
class RuleAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)