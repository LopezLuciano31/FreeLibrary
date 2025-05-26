from django.urls import path
from . import views
from .views import loginUserV

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('about/',views.about),
    path('misLibros/',views.misLibro),
    path('reader/', views.reader),
    path('login/', loginUserV, name='login'),
   path('profile/', views.profileUser, name='profile'),

]