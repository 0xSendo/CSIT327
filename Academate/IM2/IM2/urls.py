"""
URL configuration for IM2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from academate import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),
    
    # Auth-related Routes
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='landing'), name='logout'),
    path('logout/', views.custom_logout_view, name='logout'),
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
]
