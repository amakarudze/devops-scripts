from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    """Manager for user profiles."""

    def create_user(self, email, first_name, last_name, password=None):
        """Create a new user profile."""
        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        username = first_name.capitalize() + last_name.capitalize()
        user = self.model(email=email, first_name=first_name, last_name=last_name, username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Create and save a new superuser with given details."""
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
    """Database model for profiles."""
    ROLES = (
        ('Software Engineer', 'Software Engineer'),
        ('Site Reliability Engineer', 'Site Reliability Engineer'),
        ('Lead Engineer', 'Lead Engineer'),
    )
    DEPARTMENTS = (
        ('Product Development', 'Product Development'),
        ('Site Reliability Engineering', 'Site Reliability Engineering'),
        ('Implementation Engineering', 'Implementation Engineering'),
    )
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=100, choices=ROLES)
    department = models.CharField(max_length=100, choices=DEPARTMENTS)
    password = models.CharField(max_length=255)
    last_password_update = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        managed = True

    def get_full_name(self):
        """Get user's full name."""
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        """Get user's username"""
        return self.username

    def __str__(self):
        """String representation of our model in admin."""
        return self.first_name + " " + self.last_name
