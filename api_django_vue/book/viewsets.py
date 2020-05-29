"""
It allows us to make the CRUD to our model objects
"""
from rest_framework import viewsets

from .models import Book
from .serializer import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer