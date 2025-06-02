from django.urls import path
from . import views
from .views import loginUserV
from .views import registerUserV


urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('about/',views.about),
    path('reader/', views.reader),
    path('login/', loginUserV, name='login'),
    path('register/', registerUserV, name='register'),
    path('profile/', views.profileUser, name='profile'),
    path('mybooks/', views.mybooks),
    path('book_list/',views.book_list, name='book_list')
]