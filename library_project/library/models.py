from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

class User(AbstractUser):
    is_librarian = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()

    # Добавляем related_name для избежания конфликтов
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='library_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='library_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='borrowed_books')
    borrowed_date = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.title