
from rest_framework import generics

from main.models import (
    Author,
    Book,
    BookCategory,
    Tags,
    Specializations
)
from main.serializers import (
    BooksSerializer,
    AuthorSerializer
)


class BookListView(generics.ListAPIView):

    serializer_class = BooksSerializer
    # queryset = Book.objects.select_related('author', 'author__user', 'type').prefetch_related(
    #     'tags', 'author__specializations'
    # )
    queryset = Book.objects.all()
    permission_classes = ()


class AuthorListView(generics.ListAPIView):

    serializer_class = AuthorSerializer
    # queryset = Author.objects.prefetch_related('user').prefetch_related(
    #     'books', 'specializations', 'books__type', 'books__tags'
    # )
    queryset = Author.objects.all()
    permission_classes = ()
