from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from .forms import UserRegistrationForm, AssignmentForm  # Ensure you have an AssignmentForm
from .models import Assignment
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def render_home(request):
    assignments = Assignment.objects.filter(user=request.user)  # Fetch assignments for the logged-in user
    return render(request, 'home.html', {'assignments': assignments})

@csrf_protect
def render_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

@csrf_protect
def create_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.user = request.user  # Set the current user
            assignment.save()
            return redirect('home')  # Redirect to home after saving
    else:
        form = AssignmentForm()

    return render(request, 'create_assignment.html', {'form': form})

def mark_assignment_done(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    assignment.completed = True  # Mark the assignment as done
    assignment.save()
    return redirect('home')  # Redirect to home after marking done

def delete_assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    assignment.delete()  # Delete the assignment
    return redirect('home')  # Redirect to home after deletion

@login_required
def render_home(request):
    assignments = Assignment.objects.all()
    return render(request, 'home.html', {'assignments': assignments})

@login_required
def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to login page after logout