from django.contrib import admin
from django.urls import path
from academate import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),
    
    # Auth-related Routes
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout_view, name='logout'),  # Custom logout view
    path('register/', views.render_register, name='register'),
    
    # Landing Page
    path('', views.render_landing, name='landing'),
    
    # Home Page
    path('home/', views.render_home, name='home'),
    
    # Journal Routes
    path('journal/', views.journal_view, name='journal'),
    path('journal/edit/<int:entry_id>/', views.edit_journal_entry, name='edit_journal_entry'),
    path('journal/delete/<int:entry_id>/', views.delete_journal_entry, name='delete_journal_entry'),
    
    # Assignment Routes
    path('create-assignment/', views.create_assignment, name='create_assignment'),
    path('assignment/done/<int:assignment_id>/', views.mark_assignment_done, name='mark_assignment_done'),
    path('assignment/delete/<int:assignment_id>/', views.delete_assignment, name='delete_assignment'),
    
    # Navigation Route
    path('navigation/', views.render_navigation, name='navigation'),
    
    # Profile Routes
    path('profile/', views.render_profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('update-profile/', views.update_profile, name='update_profile'),  # To handle form submission from edit profile page
]
