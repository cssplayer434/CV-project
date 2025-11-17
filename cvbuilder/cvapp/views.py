

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CV, CVTemplate
from .forms import CVForm
import json

def home(request):
    templates = CVTemplate.objects.filter(active=True)
    return render(request, 'home.html', {'templates': templates})

@login_required
def dashboard(request):
    user_cvs = CV.objects.filter(owner=request.user)
    return render(request, "cvapp/dashboard.html", {"cvs": user_cvs})


@login_required
def create_cv(request):
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.owner = request.user
            cv.save()
            return redirect('dashboard')
    else:
        form = CVForm()

    return render(request, 'cvapp/create.html', {'form': form})

  

@login_required
def edit_cv(request, pk):
    cv = get_object_or_404(CV, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES, instance=cv)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CVForm(instance=cv)

    return render(request, 'cvapp/edit.html', {'form': form})

 
@login_required
def delete_cv(request, pk):
    cv = get_object_or_404(CV, pk=pk, owner=request.user)
    if request.method == 'POST':
        cv.delete()
        return redirect('dashboard')
    return render(request, 'cvapp/deleteconfirm.html', {'cv': cv})

@login_required
def preview_cv(request, pk):
    cv = get_object_or_404(CV, pk=pk, owner=request.user)
    template_slug = cv.selected_template.slug if cv.selected_template else 'classic'
    template_map = {
        'classic': 'cvapp/preview_classic.html',
        'modern': 'cvapp/preview_modern.html',
        'minimal': 'cvapp/preview_minimal.html',
    }
    template_name = template_map.get(template_slug, 'cvapp/preview_classic.html')
    # Prepare a cleaned list of skills for templates (split and strip whitespace)
    if cv.skills:
        skills = [s.strip() for s in cv.skills.split(',') if s.strip()]
    else:
        skills = []

    return render(request, template_name, {'cv': cv, 'skills': skills})
