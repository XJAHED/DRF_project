from django.db import models
from django_cleanup import cleanup
import os
# Create your models here.

def BookImagePath(instance, filename):
    extention = filename.split('.')[-1]
    filename = f"{instance.book_name}-{instance.isbn_number}.{extention}"
    return os.path.join('books/', filename)
class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

@cleanup.select
class Books(models.Model):
    book_number = models.AutoField(primary_key=True)
    isbn_number = models.CharField(max_length=13, unique=True)
    book_name = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    book_price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_quantity = models.PositiveBigIntegerField(default=1)
    image = models.ImageField( upload_to=BookImagePath, null=True, blank=True)
    
    def __str__(self):
        return self.book_name
