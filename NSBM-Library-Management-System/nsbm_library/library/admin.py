from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Author)
admin.site.register(Category)

@admin.register(Books)
class Books(admin.ModelAdmin):
    list_display = (
        'book_number',
        'book_name',
        'author',
        'book_price',
        'book_quantity'
    )