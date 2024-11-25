from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .forms import UserRegistrationForm, AssignmentForm, JournalForm
from .models import Assignment, Journal
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect


# Home view to render assignments
def render_home(request):
    assignments = Assignment.objects.filter(user=request.user)  # Fetch assignments for the logged-in user
    return render(request, 'home.html', {'assignments': assignments})

# Registration view
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

# Assignment creation view
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

# Mark assignment as done
def mark_assignment_done(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    assignment.completed = True  # Mark the assignment as done
    assignment.save()
    return redirect('home')  # Redirect to home after marking done

# Delete an assignment
def delete_assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    assignment.delete()  # Delete the assignment
    return redirect('home')  # Redirect to home after deletion

# Journal view to manage journal entries
@login_required
def journal_view(request):
    if request.method == "POST":
        form = JournalForm(request.POST)
        if form.is_valid():
            # Save the new journal entry with both title and content
            new_entry = form.save(commit=False)
            new_entry.user = request.user  # Associate the entry with the logged-in user
            new_entry.save()
            return redirect('journal')  # Redirect to the same page after saving
        else:
            # Handle form validation errors
            print("Form errors:", form.errors)
    else:
        form = JournalForm()

    # Retrieve all entries by the current user, ordered by date (most recent first)
    journal_entries = Journal.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'journal.html', {'journal_entries': journal_entries, 'form': form})

# Edit journal entry
@login_required
def edit_journal_entry(request, entry_id):
    journal_entry = get_object_or_404(Journal, id=entry_id, user=request.user)
    if request.method == 'POST':
        form = JournalForm(request.POST, instance=journal_entry)
        if form.is_valid():
            form.save()
            return redirect('journal')
    else:
        form = JournalForm(instance=journal_entry)

    return render(request, 'edit_journal_entry.html', {'form': form, 'entry': journal_entry})

# Delete journal entry
@login_required
def delete_journal_entry(request, entry_id):
    journal_entry = get_object_or_404(Journal, id=entry_id, user=request.user)
    journal_entry.delete()
    return redirect('journal')

# Logout view
def custom_logout_view(request):
    logout(request)
    return redirect('landing.html')


def render_navigation(request):
    return render(request, 'navigation.html')

# Landing page view
def render_landing(request):
    return render(request, 'landing.html')
