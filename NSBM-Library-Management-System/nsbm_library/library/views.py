import time
from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from nsbm_library.settings import EMAIL_HOST_USER
from .models import Author, Category, Books
from .serializers import AuthorSerializer, CategorySerializer, BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from email_service.views import start_library_notification

import threading
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]



class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
    search_fields = ['book_name']

class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
    search_fields = ['book_name']

    def perform_create(self, serializer):
        instance = serializer.save()
        start_library_notification(
            "New Book Added",
            f"A new book has been added to the library.\n\n"
            f"Book Name: {instance.book_name}\n"
            f"Book Discription: {instance.description}\n"
            f"Book Number: {instance.book_number}\n"
            f"Book Author: {instance.author}\n"
            f"Book Price: {instance.book_price}\n"
            
        )
        
        
    @action(detail=False, methods=['post'])
    def mail(self, request):
            subject = request.data.get('subject')
            message = request.data.get('message')
        
            if not subject or not message:
                return Response(
                    {
                        "error": "Subject and message are required."
                    },
                    status=400
                )
        
            start_library_notification(
                subject,
                message
            )
        
            return Response({
                "message": "Notification started"
            })

    