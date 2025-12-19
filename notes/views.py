from django.shortcuts import render, redirect

# Create your views here.
from .models import Note
from .forms import NoteForm
from django.views.decorators.http import require_POST


def home(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notes:home")

    else:
        form = NoteForm()

    notes = Note.objects.all().order_by("-created")
    return render(request, "home.html", {
        "form": form,
        "notes": notes,
    })


@require_POST
def delete_note(request, note_id):
    Note.objects.filter(id=note_id).delete()
    return redirect("notes:home")
