from django.contrib import admin

from main.models import (
    Author,
    Book,
    BookCategory,
    Tags,
    Specializations
)

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookCategory)
admin.site.register(Tags)
admin.site.register(Specializations)
