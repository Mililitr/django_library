from django.urls import path
from .views import (
    book_list, my_books, librarian_dashboard, register_reader,
    register_librarian, user_login, borrow_book, return_book, user_logout
)

urlpatterns = [
    path('', book_list, name='book_list'),
    path('my-books/', my_books, name='my_books'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('register-reader/', register_reader, name='register_reader'),
    path('register-librarian/', register_librarian, name='register_librarian'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),  # Изменено на 'logout'
    path('borrow-book/<int:book_id>/', borrow_book, name='borrow_book'),
    path('return-book/<int:book_id>/', return_book, name='return_book'),
]