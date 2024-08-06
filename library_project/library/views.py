import logging
from datetime import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Book, User
from .forms import ReaderRegistrationForm, LibrarianRegistrationForm


def book_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'library/book_list.html', {'books': books})

@login_required
def my_books(request):
    books = Book.objects.filter(borrower=request.user).order_by('title')
    return render(request, 'library/my_books.html', {'books': books})

@login_required
def librarian_dashboard(request):
    if request.user.is_librarian:
        debtors = User.objects.filter(borrowed_books__isnull=False).distinct()
        return render(request, 'library/librarian_dashboard.html', {'debtors': debtors})
    return redirect('book_list')

def register_reader(request):
    if request.method == 'POST':
        form = ReaderRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_librarian = False
            user.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = ReaderRegistrationForm()
    return render(request, 'registration/register_reader.html', {'form': form})

def register_librarian(request):
    if request.method == 'POST':
        form = LibrarianRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_librarian = True
            user.save()
            login(request, user)
            return redirect('librarian_dashboard')
    else:
        form = LibrarianRegistrationForm()
    return render(request, 'registration/register_librarian.html', {'form': form})

logger = logging.getLogger(__name__)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                login(request, user)
                if user.is_librarian:
                    return redirect('librarian_dashboard')
                else:
                    return redirect('book_list')
            except IntegrityError as e:
                logger.error(f"IntegrityError during login: {e}")
                return render(request, 'registration/login.html', {'error': 'Database error occurred. Please try again.'})
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid username or password.'})
    return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('book_list')

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.borrower = request.user
    book.borrowed_date = timezone.now()
    book.save()
    return redirect('book_list')

@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.borrower = None
    book.borrowed_date = None
    book.save()
    return redirect('book_list')
