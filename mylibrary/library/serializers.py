from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"



class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  
        fields = [
            "title", 
            "author", 
            "description"
        ]  
