from .models import Task, Country, Capital, Author, Book, AuthorBook
from django.contrib import admin

# Register your models here.
admin.site.register(Task)
admin.site.register(Country)
admin.site.register(Capital)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(AuthorBook)

