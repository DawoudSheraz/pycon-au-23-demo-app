
import datetime

from django.contrib.auth import get_user_model
import factory.fuzzy
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

    name = factory.fuzzy.FuzzyText()

    class Meta:
        model = Specializations


class TagsFactory(DjangoModelFactory):

    name = factory.fuzzy.FuzzyText()

    class Meta:
        model = Tags


class BookCategoryFactory(DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()

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

    title = factory.fuzzy.FuzzyText()
    description = factory.fuzzy.FuzzyText()
    author = SubFactory(AuthorFactory)
    type = SubFactory(BookCategoryFactory)
    publish_date = factory.fuzzy.FuzzyDateTime(datetime.datetime(2008, 1, 1, tzinfo=datetime.timezone.utc))

    class Meta:
        model = Book

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        self.tags.add(*extracted)
