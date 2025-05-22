from django.contrib import admin
from .models import Autor, Book, Credential, User, Edition

# Register your models here.
admin.site.register(Autor)
admin.site.register(Book)
admin.site.register(Credential)
admin.site.register(User)
admin.site.register(Edition)