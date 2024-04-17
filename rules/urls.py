from . import views
from django.urls import path

urlpatterns = [
    path('rules.html', views.rules, name='rules'),
]