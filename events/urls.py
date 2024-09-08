from . import views
from django.urls import path
from .views import EventDeleteView, EventUpdateView

urlpatterns = [
    path("", views.EventList.as_view(), name="events"),
    path('event/<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
    path('create/', views.create_event, name='create_event'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('event/<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
]