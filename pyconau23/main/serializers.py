from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from main.models import (
    Author,
    Book,
    BookCategory,
    Tags,
    Specializations
)


User = get_user_model()


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class BookTypeSerializer(ModelSerializer):

    class Meta:
        model = BookCategory
        fields = ('name', )


class SpecializationsSerializer(ModelSerializer):

    class Meta:
        model = Specializations
        fields = ('name', 'slug')


class TagsSerializer(ModelSerializer):

    class Meta:
        model = Tags
        fields = ('name', 'slug')


class MinimalBookSerializer(ModelSerializer):
    """
    Book serializer without author information, to be used within Author serializer.
    """
    tags = SlugRelatedField(slug_field='slug', queryset=Tags.objects.all(), many=True)
    type = BookTypeSerializer()

    class Meta:
        model = Book
        fields = ('title', 'description', 'published', 'publish_date', 'tags', 'type')


class AuthorSerializer(ModelSerializer):

    books = MinimalBookSerializer(many=True)
    user = UserSerializer()
    specializations = SlugRelatedField(slug_field='slug', queryset=Specializations.objects.all(), many=True)

    class Meta:
        model = Author
        fields = ('user', 'specializations', 'date_of_birth', 'books')
