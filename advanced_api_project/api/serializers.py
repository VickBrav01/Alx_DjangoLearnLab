from rest_framework import serializers
from .models import Book, Author
from datetime import datetime


# BookSerializer that serializes all fields of the Book model.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    # Custom validation to the BookSerializer to ensure the publication_year is not in the future.
    def validate(self, data):
        if data["publication_year"] > datetime.now():
            raise serializers.ValidationError("Date cannot be in the future")
        return data


# AuthorSerializer that includes:The name field &
# a nested BookSerializer to serialize the related books dynamically
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]
