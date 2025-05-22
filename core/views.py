from django.shortcuts import render
from django.http import HttpResponse
from .models import Autor, Book, Credential, User, Edition

# Create your views here.
def homepage(request):
    editions_for_html = Edition.objects.all()
    return render(request, "homepage.html", {'editions':editions_for_html})

def about(request):
    return HttpResponse("<h3>Aqui esta About</h3>")

def misLibro(request):
    return HttpResponse("<h1>Aqui estan tus libros</h1>")

def reader(request):
    return render(request, 'reader.html')