from django.forms import ModelForm
from .models import _

class EditionForm(ModelForm):
    class Meta:
        model = Edition
        fields = ["id","title", "publicationDate","publisher","lang","pages","notes","place","cover","file","of"]

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["id","name", "description", "publicationDate","genres","autor"]

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ["name", "lastName", "bio","birth","death","prof","portrait"]
    