from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Author, Book


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, value):
        return value.name

    class Meta:
        model = Author
        fields = ['name']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = AuthorSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = ['title', 'edition', 'publication_year', 'authors']
