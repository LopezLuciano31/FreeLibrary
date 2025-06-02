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

def mybooks(request):
    return render(request, 'mybooks.html')

def reader(request):
    return render(request, 'reader.html')

def profileUser(request):
     return render(request, 'profile.html')
     
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

def registerUserV(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        pwd2 = request.POST.get("password2")
        email = request.POST.get("email")
        if pwd != pwd2:
            return redirect('homepage')
        if User.objects.filter(username=username).exists():
            return redirect('homepage')
        try:
            user = User.objects.create_user(username=username, password=pwd, email=email)
            user.save()
            login(request, user)  
            return redirect(reverse('homepage') + '?success=true')
        except Exception as e:
            messages.error(request, f"Error al registrar: {str(e)}")
            return redirect('homepage')
    else:
        return redirect('homepage')
    
def book_list(request):
    books = Book.objects.prefetch_related('edition_set').all()

    filter_by = request.GET.get("filter_by")
    query = request.GET.get("query")

    if filter_by and query:
        if filter_by == "title":
            books = books.filter(name__icontains=query)
        elif filter_by == "author":
            books = books.filter(autor__name__icontains=query)
        elif filter_by == "description":
            books = books.filter(description__icontains=query)
        elif filter_by == "genres":
            books = books.filter(genres__icontains=query)
    
    context = {
        "books": books,
        "filter_by": filter_by,
        "query": query,
    }
    return render(request, "book_list.html", context)

def bookRegister(request):
    if request.method == "POST":
     autorName= request.POST.get("autor")
     book = Book (id= request.POST.get("id"), name = request.POST.get("name"), description = request.POST.get("description"), 
     publicationDate = request.POST.get("publicationDatename"), genres= request.POST.get("genres"), autor= Autor.objects.get(name=autorNames))
     book.save()

def autorRegister(request):
  if request.method == "POST":
     autor = Autor ( name = request.POST.get("name"), lastName = request.POST.get("lastName"), 
     bio = request.POST.get("bio"), birth= request.POST.get("birth"), death= request.POST.get("death"),
     prof = request.POST.get("prof"), portrait= request.POST.get("portrait"))
     autor.save()
    

def editionRegister(request):
    if request.method == "POST":
     book= request.POST.get("of")
     edi = Edition (id= request.POST.get("id"), title = request.POST.get("title"), description = request.POST.get("description"), 
     publicationDate = request.POST.get("publicationDatename"), publisher= request.POST.get("publisher"), 
     lang = request.POST.get("lang"), pages= request.POST.get("pages"), notes = request.POST.get("notes"), 
     place= request.POST.get("place"),  cover = request.POST.get("cover"), file= request.POST.get("file"),
     of= Book.objects.get(id=book)
     )
     edi.save()
