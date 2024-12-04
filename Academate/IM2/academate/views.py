from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .forms import UserRegistrationForm, AssignmentForm, JournalForm
from .models import Assignment, Journal
from django.contrib.auth import login, logout  # Ensure login is imported
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Profile 


# Home view to render assignments
def render_home(request):
    assignments = Assignment.objects.filter(user=request.user)
    username = request.user.username
    # Access course and year_level directly from the User model
    course = request.user.course or 'Unknown'  # Use default 'Unknown' if course is None
    year_level = request.user.year_level or 'Unknown'  # Use default 'Unknown' if year_level is None
    return render(request, 'home.html', {
        'assignments': assignments,
        'username': username,
        'course': course,
        'year_level': year_level
    })

# Registration view
@csrf_protect
def render_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create the user with the provided fields
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Save the user object

            # Create a profile for the user
            Profile.objects.create(user=user)  # You can set default values for profile fields if needed

            # Optionally, you can log the user in automatically
            login(request, user)
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # Redirect to home or wherever after successful login
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

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
    return redirect('landing')  # Correct the redirect to the URL name

# Navigation view (if applicable)
def render_navigation(request):
    return render(request, 'navigation.html')

# Landing page view
def render_landing(request):
    return render(request, 'landing.html')

# Profile view (if applicable)
def render_profile(request):
    user = request.user  # Get the logged-in user
    return render(request, 'profile.html', {'user': user})

def edit_profile(request):
    return render(request, 'profile.html')



def update_profile(request):
    user = request.user  # Fetch the logged-in user

    if request.method == 'POST':
        # Safely update user fields with provided data
        user.first_name = request.POST.get('name', user.first_name)
        user.course = request.POST.get('course', getattr(user, 'course', ''))
        user.address = request.POST.get('address', getattr(user, 'address', ''))
        user.birthdate = request.POST.get('birthdate', user.birthdate)
        user.username = request.POST.get('username', user.username)

        # Handle password update
        password = request.POST.get('password')
        if password:
            user.set_password(password)

        # Save the updated user object
        user.save()

        # Add a success message
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')  # Redirect to profile page to reload the data with the updated user

    # Render the form with the current user data
    return render(request, 'profile.html', {'user': user})
    
def some_view(request):
    if not request.user.is_authenticated:
        return redirect('login') 


# Delete journal entry
@login_required
def delete_journal_entry(request, entry_id):
    journal_entry = get_object_or_404(Journal, id=entry_id, user=request.user)
    journal_entry.delete()
    return redirect('journal')

@login_required
def delete_journal_entry(request, entry_id):
    try:
        journal_entry = get_object_or_404(Journal, id=entry_id, user=request.user)
        journal_entry.delete()
        return redirect('journal')
    except Exception as e:
        print(f"Error deleting journal entry: {e}")
        return redirect('journal')
