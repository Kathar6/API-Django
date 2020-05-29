"""
This file serializes the models that we want to use in the API, to be sent by the HTTP method
"""
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # __all__ : Work with all the fields of the model
        fields = '__all__'