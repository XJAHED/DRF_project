from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from .models import *
from rest_framework.permissions import AllowAny
# Create your views here.


class room(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]

class study_room(viewsets.ModelViewSet):
    queryset = StudyRoom.objects.all()
    serializer_class = StudyRoomSerializer
    permission_classes = [AllowAny]