from django.contrib import admin
from .models import Autor, Book, Edition

# Register your models here.
admin.site.register(Autor)
admin.site.register(Book)
admin.site.register(Edition)