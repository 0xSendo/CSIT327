from django import forms
from django.contrib.auth.hashers import make_password
from .models import User, Assignment
from .models import Journal
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=True, 
        error_messages={'required': 'Password is required.'} 
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirm Password',
        required=True,  
        error_messages={'required': 'Please confirm your password.'}  
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # Hash the password

        if commit:
            user.save()  

        return user

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['name', 'due_date']
    
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date < timezone.now().date():
            raise forms.ValidationError("Due date cannot be in the past.")
        return due_date
class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['title', 'content']