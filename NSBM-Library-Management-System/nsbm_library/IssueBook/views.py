from django.shortcuts import render
from .serializers import IssueSerializer
from .models import *
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
# Create your views here.


class IssueViewSet(viewsets.ModelViewSet):
    queryset = IssueBook.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [AllowAny]