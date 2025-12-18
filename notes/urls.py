from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("delete/<int:note_id>/", views.delete_note),
]
