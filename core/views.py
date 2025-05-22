from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    books(request)
    return render(request, "homepage.html")

def about(request):
    return HttpResponse("<h3>Aqui esta About</h3>")

def misLibro(request):
    return HttpResponse("<h1>Aqui estan tus libros</h1>")

def books(request):
    #Libros en tendencia
    #libros clasicos
    return 