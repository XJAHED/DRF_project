from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Author, Category, Books
from .serializers import AuthorSerializer, CategorySerializer, BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.db import connections
import threading
# Create your views here.


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


def send_book_created(book_number, book_name):
    try:
        for book in Books.objects.all():
            print(book.book_number, book.book_name)
    finally:
        connections.close_all()
class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
    search_fields = ['book_name']
    def perform_create(self, serializer):
        isinstance = serializer.save()
        thread = threading.Thread(
            target=send_book_created,
            args=(isinstance.book_number, isinstance.book_name)
        )
        thread.daemon = True
        thread.start()
    