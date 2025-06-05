from django.forms import ModelForm
from .models import *
from django import forms

class EditionForm(ModelForm):
    class Meta:
        model = Edition
        fields = ["id","title", "publicationDate","publisher","lang","pages","notes","place","cover","file","of"]
        widgets = {
            'publicationDate': forms.DateInput(attrs={'type': 'date'}),
        }

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["id","name", "description", "publicationDate","genres","autor"]
        widgets = {
            'publicationDate': forms.DateInput(attrs={'type': 'date'}),
        }

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ["name", "lastName", "bio","birth","death","prof","portrait"]
        widgets = {
            'birth': forms.DateInput(attrs={'type': 'date'}),
            'death': forms.DateInput(attrs={'type': 'date'})  
        }

