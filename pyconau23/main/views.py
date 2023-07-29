
from rest_framework import generics

from main.models import (
    Author,
    Book,
    BookCategory,
    Tags,
    Specializations
)
from main.serializers import (
    MinimalBookSerializer,
    AuthorSerializer
)


class BookListView(generics.ListAPIView):

    serializer_class = MinimalBookSerializer
    queryset = Book.objects.all()
    permission_classes = ()


class AuthorListView(generics.ListAPIView):

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = ()
