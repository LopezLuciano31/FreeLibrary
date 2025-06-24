from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Autor, Book, Edition, Review, Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import *
from django.core.mail import send_mail
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db.models import Avg
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.
def bookfav(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    idEdition = request.GET.get('edition')
    bookEdition = Edition.objects.get(id=idEdition)
    if (profile.favorites.filter(id=idEdition).exists()):
        profile.favorites.remove(bookEdition)
        return JsonResponse({
                'success': False,
            })
    else:
        profile.favorites.add(bookEdition)
        return JsonResponse({
                'success': True,
            })
 

def logoutV(request):
    logout(request)
    url = request.POST.get('returnUrl', '/')
    return redirect(url)

def homepage(request):
    editions_for_html = Edition.objects.all()
    return render(request, "homepage.html", {'editions':editions_for_html})

def about(request):
    return HttpResponse("<h3>Aqui esta About</h3>")

def mybooks(request):
    return render(request, 'mybooks.html')

def reader(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        bookEdition = request.GET.get('edition')
        fav = profile.favorites.filter(id=bookEdition).exists()
        bookEdition = Edition.objects.get(id=bookEdition)
        profile.reading.add(bookEdition)
        return render(request, 'reader.html' ,{'fav': fav})
    return render(request, 'reader.html')

def profileUser(request):
     return render(request, 'profile.html')

def loginUserV(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
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
        bookReview = request.GET.get('book')
        bookReview = Book.objects.get(id=bookReview)
        review= Review.objects.get(user=request.user, book=bookReview)
        response = {
        'content': review.content,
        'rating': review.rating
        }
        return JsonResponse({'success': True, 'review':response})
    except Review.DoesNotExist:
        return JsonResponse({'success': False})

    

def reviewForm(request):
        if request.method == "POST":
         textReview = request.POST.get("review")
         ratingReview = request.POST.get("rating")
         bookReview = request.POST.get("book")
         bookReview = Book.objects.get(id=bookReview)
         userReview = request.user
         try:
             review = Review.objects.get(user=userReview, book=bookReview)
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
    edition = Edition.objects.filter(title__icontains=title)
    bookReview = request.GET.get('book')
    bookReview = Book.objects.get(id=bookReview)
    ratingBook= Review.objects.filter(book=bookReview).aggregate(avg=Avg('rating'))['avg'] or 0.0
    return render(request, 'bookprofile.html', {'edition': edition, 'ratingBookProfile': int(ratingBook)})

def registerUserV(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        pwd2 = request.POST.get("password2")
        email = request.POST.get("email")
        verification = False
        error = []
        errorCode= []
        try:
            validate_password(pwd)
        except ValidationError as e:
            for message in e.messages:
              error.append([message, "pwdError"])
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
            profile= Profile(user=user)
            profile.save()
            login(request, user) 
            subject = "Bienvenido a FreeLibrary"
            from_email = settings.EMAIL_HOST_USER
            to = [email]
            context = {'username': username}
            html_content = render_to_string('registration/register_Email.html', context)
            text_content = f"Hola {username}, bienvenido a FreeLibrary!"
            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(html_content, "text/html")
            msg.send() 
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
