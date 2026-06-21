from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
class Books(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    quantity = models.PositiveBigIntegerField(default=1)
    
    def __str__(self):
        return self.title
    