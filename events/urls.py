from . import views
from django.urls import path

urlpatterns = [
    path("", views.EventList.as_view(), name="events"),
    path('event/<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
]