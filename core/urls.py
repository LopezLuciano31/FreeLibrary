from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('about/',views.about),
    path('misLibros/',views.misLibro),
    path('reader/', views.reader),
]