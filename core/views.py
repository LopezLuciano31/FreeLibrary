from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

def about(request):
    return HttpResponse("<h3>Aqui esta About</h3>")