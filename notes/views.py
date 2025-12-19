from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Note
from .forms import NoteForm
from django.views.decorators.http import require_POST


@login_required
def home(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("notes:home")

    else:
        form = NoteForm()

    notes = Note.objects.filter(user=request.user).order_by("-created")
    return render(request, "home.html", {
        "form": form,
        "notes": notes,
    })


@require_POST
def delete_note(request, note_id):
    Note.objects.filter(id=note_id, user=request.user).delete()
    return redirect("notes:home")
