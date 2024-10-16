from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

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
