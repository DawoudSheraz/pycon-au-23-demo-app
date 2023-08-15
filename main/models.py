from django.db import models
from django.contrib.auth import get_user_model

from autoslug import AutoSlugField


User = get_user_model()


class AbstractNameSlugModel(models.Model):
    name = models.CharField(max_length=32)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        abstract = True

    def __str__(self):
        return self.slug


class Specializations(AbstractNameSlugModel):
    pass


class Tags(AbstractNameSlugModel):
    pass


class BookCategory(models.Model):
    name = models.CharField(max_length=64)


class Author(models.Model):
    user = models.OneToOneField(User, related_name="author", on_delete=models.CASCADE)
    specializations = models.ManyToManyField(Specializations)
    date_of_birth = models.DateTimeField(auto_now=False)


class Book(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    published = models.BooleanField(default=False)
    publish_date = models.DateField(auto_now=False, null=True)
    # Assume book can only have one author and is of a single type (horror, thriller)
    # this is only for simplicity
    author = models.ForeignKey(Author, related_name="books", on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(BookCategory, related_name="books", on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tags)


