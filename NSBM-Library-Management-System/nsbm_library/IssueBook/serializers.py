from rest_framework import serializers
from .models import *
from AddMember.serializers import AddMemberSerializer
from AddMember.models import *
from library.serializers import BookSerializer
from library.models import *

class IssueSerializer(serializers.ModelSerializer):
    member = AddMemberSerializer(read_only=True)
    book = BookSerializer(read_only=True)
    
    member_post = serializers.PrimaryKeyRelatedField(
        queryset = AddMember.objects.all(),
        source = "member",
        write_only = True
    )
    
    book_post = serializers.PrimaryKeyRelatedField(
            queryset = Books.objects.all(),
            source = "book",
            write_only = True
        )
    
    class Meta:
        model = IssueBook
        fields = [
            'member',
            'member_post',
            'book',
            'book_post',
            'issue_date',
            'due_date',
            'is_returned',
            'return_date'
        ]
