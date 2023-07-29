
from django.urls import path

from main.views import (
    AuthorListView,
    BookListView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('authors/', AuthorListView.as_view(), name='author-list')
]
