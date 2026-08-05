from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import AddMemberSerializer
# filter

from rest_framework.filters import SearchFilter

# Create your views here.
class memberviewset(viewsets.ModelViewSet):
    queryset = AddMember.objects.all()
    serializer_class = AddMemberSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['Member_name', 'member_id', 'postion', 'department', 'batch']
    