from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class signup(APIView):
    def post(self, request):
        serializer = signupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                 "message": "Account created successfully"
            },
            status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmailTokenView(TokenObtainPairView):
    serializer_class=EmailTokenSerializer