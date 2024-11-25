from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

# User Manager
class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username or not password:
            raise ValueError('Please fill the fields!')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)

# Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=30)  # New field
    last_name = models.CharField(max_length=30)   # New field
    is_staff = models.BooleanField(default=False)  

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']  

    objects = UserManager()

    def __str__(self):
        return self.username

# Assignment Model
class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link assignment to a user
    name = models.CharField(max_length=255)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Journal Model
class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
