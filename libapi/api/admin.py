from django.contrib import admin
from .models import Book, Author, BookAuthor

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookAuthor)
