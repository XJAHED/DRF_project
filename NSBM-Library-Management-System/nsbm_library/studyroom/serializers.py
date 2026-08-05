from rest_framework import serializers
from .models import StudyRoom, Room
from AddMember.models import AddMember


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddMember
        fields = '__all__'


class StudyRoomSerializer(serializers.ModelSerializer):
    member_name = MemberSerializer(read_only=True)
    room_no = RoomSerializer(read_only=True)
    
    member_name_post = serializers.PrimaryKeyRelatedField(
        queryset = AddMember.objects.all(),
        source = "member_name",
        write_only = True
    )
    
    room_no_post = serializers.PrimaryKeyRelatedField(
        queryset = Room.objects.all(),
        source = "room_no",
        write_only = True
    )
    
    class Meta:
        model = StudyRoom
        fields = [
            'id',
            'member_name',
            'room_no',
            'date',
            'time',
            'member_name_post',
            'room_no_post'
        ]