from django.contrib import admin
from .models import Book, Author  # Import models after they are defined

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)