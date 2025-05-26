from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Autor, Book, Edition
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse

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

def loginUserV(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("DEBUG:", username, password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('homepage') + '?success=true') 
        else:
            messages.error(request, "Credenciales inválidas")
            return redirect('homepage')
    else:
        return redirect('homepage')