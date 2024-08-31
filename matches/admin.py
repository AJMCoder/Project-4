from django.contrib import admin
from .models import Match

class MatchAdmin(admin.ModelAdmin):
    list_display = ('player1', 'player2', 'score', 'date_played')
    search_fields = ('player1__username', 'player2__username', 'score')
    list_filter = ('date_played',)

admin.site.register(Match, MatchAdmin)