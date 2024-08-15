from django.shortcuts import render
from .models import Notes
from .forms import NotesForm
from django.contrib.auth.models import User


# Create your views here.

def all_notes(request):
    all_notes = Notes.objects.all()
    
    context = {
        'all_notes' : all_notes
    }
    
    return render(request, 'all_notes.html', context)



def detail(request , slug):
    note = Notes.objects.get(slug=slug)
    
    context = {
        'note' : note
    }
    
    return render(request, 'note_detail.html', context)


def note_add(request):
    
    form = NotesForm()  
    
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
    
    
    context = {
        'form' : form,
    }
    
    return render(request, 'add.html', context)
