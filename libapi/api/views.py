from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book
from .pagination import StandardResultsSetPagination


class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'edition', 'authors__name']


class AuthorFilter(filters.FilterSet):
    class Meta:
        model = Author
        fields = ['name']


class AuthorViewSet(viewsets.ModelViewSet):

    """
    API endpoint that list all authors.
    """
    queryset = Author.objects.all()
    serializer = AuthorSerializer(queryset, many=True)
    serializer_class = AuthorSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AuthorFilter


class BookViewSet(viewsets.ModelViewSet):

    """
    API endpoint that list all authors.
    """
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter
