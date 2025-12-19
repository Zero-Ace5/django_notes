from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path("", views.home, name="home"),
    path("delete/<int:note_id>/", views.delete_note, name="delete_note"),
]
