from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class ReaderRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'address', 'password1', 'password2')

class LibrarianRegistrationForm(UserCreationForm):
    employee_number = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'employee_number', 'password1', 'password2')