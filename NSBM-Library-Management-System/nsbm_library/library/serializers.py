from rest_framework import serializers
from .models import Author, Category, Books

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    
    author_post = serializers.PrimaryKeyRelatedField(
        queryset = Author.objects.all(),
        source = "author",
        write_only = True
    )
    category_post = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        source = "category",
        write_only = True
    )

    class Meta:
        model = Books
        fields = [
            "book_number",
            "book_name",
            "isbn_number",
            "purchase_date",
            "description",
            "book_quantity",
            "image",
            "book_price",
            "author",
            "author_post",
            "category",
            "category_post",
        ]