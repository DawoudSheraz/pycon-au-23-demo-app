
import datetime

import factory.fuzzy
from django.contrib.auth import get_user_model
from factory import SubFactory
from factory.django import DjangoModelFactory

from main.models import (
    Author,
    Book,
    BookCategory,
    Tags,
    Specializations
)

User = get_user_model()


class SpecializationFactory(DjangoModelFactory):

    class Meta:
        model = Specializations


class TagsFactory(DjangoModelFactory):
    class Meta:
        model = Tags


class BookCategoryFactory(DjangoModelFactory):
    class Meta:
        model = BookCategory


class UserFactory(DjangoModelFactory):

    email = factory.fuzzy.FuzzyText(suffix='@example.com')
    username = factory.fuzzy.FuzzyText(prefix="username_")

    class Meta:
        model = User


class AuthorFactory(DjangoModelFactory):

    user = SubFactory(UserFactory)
    date_of_birth = factory.fuzzy.FuzzyDateTime(datetime.datetime(2008, 1, 1, tzinfo=datetime.timezone.utc))

    class Meta:
        model = Author

    @factory.post_generation
    def specializations(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        self.specializations.add(*extracted)


class BookFactory(DjangoModelFactory):

    author = SubFactory(AuthorFactory)
    type = SubFactory(BookCategoryFactory)

    class Meta:
        model = Book

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        self.tags.add(*extracted)
