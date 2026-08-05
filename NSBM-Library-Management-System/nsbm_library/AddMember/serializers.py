from rest_framework import serializers
from .models import *

class AddMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddMember
        fields = '__all__'