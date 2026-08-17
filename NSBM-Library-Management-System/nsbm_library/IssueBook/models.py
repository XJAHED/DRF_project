from django.db import models
from AddMember.models import AddMember
from library.models import Books
# Create your models here.

class IssueBook(models.Model):
    member = models.ForeignKey(AddMember, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    is_returned = models.BooleanField(default=False)
    
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.member} - {self.book}"