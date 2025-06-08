from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Autor, Book, Edition
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import *
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib.auth import logout

# Create your views here.
def logoutV(request):
    logout(request)
    return redirect('homepage')

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
            return JsonResponse({
                'success': True,
                'redirect_url': '/'  
            })
        else:
            return JsonResponse({
                'success': False,
                'error': "Credenciales inválidas"
            })
    return JsonResponse({'success': False, 'error': "Método no permitido"})

def review(request):
    try:
        review= Review.objects.get(user=request.user)
        return render(request, 'testTemplate/formReview.html', {'review': review})
    except Review.DoesNotExist:
        return render(request, 'testTemplate/formReview.html')
 

 
def reviewForm(request):
        if request.method == "POST":
         textReview = request.POST.get("review")
         ratingReview = request.POST.get("rating")
         bookReview = request.POST.get("book")
         bookReview = Book.objects.get(id=bookReview)
         userReview = request.user
         try:
             review = Review.objects.get(user=userReview)
         except Review.DoesNotExist:
             review = None 
         if ratingReview and textReview and float(ratingReview) != 0:
            if review is not None:
              review.rating=ratingReview
              review.content=textReview
            else:
              review = Review(
                  content=textReview,
                  user=userReview,
                  book=bookReview,  
                  rating=ratingReview
                    )
            review.save()
            return JsonResponse({'success': True, 'redirect_url': '/'})
         else:
            return JsonResponse({
                'success': False,
                'error': "Debe seleccionar una puntuación y escribir una reseña"
            })
        return JsonResponse({'success': False, 'error': "Método no permitido"})

def bookprofile(request, title):
    return  render(request, 'bookprofile.html')

def registerUserV(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        pwd2 = request.POST.get("password2")
        email = request.POST.get("email")
        verification = False
        error = []
        errorCode= []
        if len(pwd) < 8:
            verification = True;
            error.append(["La contrasena debe tener minimo 8 caracteres","pwdLenghtError"])
        if pwd != pwd2:
             verfication = True;
             error.append(["Contrasenas no coinciden","pwdError"])
        if username!= "" and User.objects.filter(username=username).exists():
             verfication=True
             error.append(["Nombre de usuario ya registrado","usertError"])
        if username == "":
             verification=True;
             error.append(["*Campo obligatorio","userError"])     
        if email != "" and User.objects.filter(email=email).exists():
             verification=True;
             error.append(["Email de usuario ya registrado","emailError"])
        if email == "":
             verification=True;
             error.append(["*Campo obligatorio","emailError"])
        if (verification):
            return JsonResponse({
                'success': False,
                'error': error,
            })
        try:
            user = User.objects.create_user(username=username, password=pwd, email=email)
            user.save()
            login(request, user)  
            return JsonResponse({
                'success': True,
                'redirect_url': '/'  
            })
        except Exception as e:
            messages.error(request, f"Error al registrar: {str(e)}")
            return JsonResponse({
                'success': False,
                'error': "Error al registrar, intentelo nuevamente"  
            })
    else:
         return JsonResponse({
                'success': False,
                'error': "Error, metodo de envio invalido"  
            })
    
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
     form = BookForm(request.POST)
     if form.is_valid():
        form.save()         
        return redirect('homepage')
 else:
          form = BookForm()
 return render(request,"mybooks.html",{'form':form})


def autorRegister(request):
  if request.method == "POST":
     form = AutorForm(request.POST, request.FILES)
     if form.is_valid():
        form.save()
        return redirect('homepage')
  else:
      form = AutorForm()
      
  return render(request,"mybooks.html",{'form3':form})
     
    

def editionRegister(request):
 if request.method == "POST":
     form = EditionForm(request.POST, request.FILES)
     if form.is_valid():
        form.save()
        return redirect('homepage')
 else:         
     form = EditionForm()
 return render(request,"mybooks.html",{'form2':form})

