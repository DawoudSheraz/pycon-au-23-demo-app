
from rest_framework import generics

from main.models import (
    Author,
    Book,
)
from main.serializers import (
    BooksSerializer,
    AuthorSerializer
)


class BookListView(generics.ListAPIView):

    serializer_class = BooksSerializer
    # queryset = Book.objects.all()
    queryset = Book.objects.select_related('author', 'author__user', 'type').prefetch_related(
        'tags', 'author__specializations'
    )
    permission_classes = ()


class AuthorListView(generics.ListAPIView):

    serializer_class = AuthorSerializer
    # queryset = Author.objects.all()
    queryset = Author.objects.select_related('user').prefetch_related(
        'books', 'specializations', 'books__tags', 'books__type'
    )
    permission_classes = ()
