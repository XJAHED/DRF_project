from django.db import models
from AddMember.models import AddMember
# Create your models here.


class Room(models.Model):
    room_no = models.CharField(max_length=50)
    def __str__(self):
        return self.room_no

class StudyRoom(models.Model):
    member_name = models.ForeignKey(AddMember, on_delete=models.CASCADE)
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return self.room_no