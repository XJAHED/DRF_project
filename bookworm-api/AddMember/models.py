from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class AddMember(models.Model):
    Member_name = models.CharField(max_length=150)
    member_id = models.CharField(max_length=50, unique=True)
    postion = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    batch = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.Member_name