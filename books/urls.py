from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.list_books, name='list_books'),
    path('books/<int:book_id>/', views.book_details, name='book_details'),
]