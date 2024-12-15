from django.shortcuts import render
from .models import Book

# View for the homepage
def home(request):
    return render(request, 'home.html')

# View for the list of books
def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'list_books.html', {'books': books})

# View for the details of a single book
def book_details(request, book_id):
    book = Book.objects.get(id=book_id)  # Get the book by its ID
    return render(request, 'book_details.html', {'book': book})
