from django.forms import ModelForm
from .models import *
from django import forms

class EditionForm(ModelForm):
    class Meta:
        model = Edition
        fields = ["id","title", "publicationDate","publisher","lang","pages","notes","place","cover","file","of"]
        labels = {
            'title': 'Titulo edicion:',
            'lang': 'Lenguaje:',
            'publicationDate': 'Fecha de publlicacion:',
            'pages': 'Numero de paginas:',
            'id':'Identificador numerico:',
            'cover':'Portada:',
            'file':'Archivo:',
            'publisher':'Editorial:',
            'notes':'Notas:',
            'place':'Lugar:',
            'of':'Libro:'
        }
        widgets = {
            'publicationDate': forms.DateInput(attrs={ 'type': 'date',}),}

      
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["id","name", "description", "publicationDate","genres","autor"]
        labels = {
            'name': 'Titulo:',
            'description': 'Descripcion:',
            'publicationDate': 'Fecha de publlicacion:',
            'autor': 'Autor:',
            'id':'Identificador numerico:',
            'genres':'Generos:'
        }
        widgets = {
            'publicationDate': forms.DateInput(attrs={ 'type': 'date',}),}


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ["name", "lastName", "bio","birth","death","prof","portrait"]
        labels = {
            'name': 'Nombre:',
            'lastName': 'Apellido:',
            'bio': 'Biografia:',
            'prof': 'Profesion:',
            'portrait': 'Retrato:',
            'birth': 'Fecha de nacimiento',
            'death': 'Fecha de defuncion',
        }
        widgets = {
            'birth': forms.DateInput(attrs={  'type': 'date' }),
            'death': forms.DateInput(attrs={  'type': 'date' }),
        } 