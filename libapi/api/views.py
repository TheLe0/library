from django.contrib.auth.models import User, Group
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, AuthorSerializer
from .models import Author
from .pagination import StandardResultsSetPagination


class AuthorFilter(filters.FilterSet):
    class Meta:
        model = Author
        fields = ['name']


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticated]


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
