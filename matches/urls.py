# matches/urls.py
from django.urls import path
from .views import submit_match, recent_matches

urlpatterns = [
    path('submit/', submit_match, name='submit_match'),
    path('recent/', recent_matches, name='recent_matches'),
]