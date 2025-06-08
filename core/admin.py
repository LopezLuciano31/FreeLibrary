from django.contrib import admin
from .models import Autor, Book, Edition, Review

# Register your models here.
admin.site.register(Autor)
admin.site.register(Book)
admin.site.register(Edition)
admin.site.register(Review)