from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import ListCreateAPIView

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Category, Author, Books
from .serializers import CategorySerializer, AuthorSerializer, BookSerializer

# filter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


# !Api view set
# class BookListView(APIView):
#     def get(self, request):
#         books = Books.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#! Generic view set
# class BooklistCreateView(ListCreateAPIView):
#     queryset = Books.object.all()
#     serializer_class = BookSerializer


#! Model view set
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ('category', 'author')

