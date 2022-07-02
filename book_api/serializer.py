from dataclasses import fields
from rest_framework import serializers
from book_api.models import Book

class BookSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField()
    #title = serializers.CharField()
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publish_date']

    #add validation here
    #def validate(self, data):
        #pass