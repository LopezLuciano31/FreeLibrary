from django.urls import path
from . import views
from .views import loginUserV
from .views import registerUserV
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('about/',views.about),
    path('reader/', views.reader),
    path('login/', loginUserV, name='login'),
    path('register/', registerUserV, name='register'),
    path('autorRegister/', views.autorRegister, name='autorRegister'),
    path('bookRegister/', views.bookRegister, name='bookRegister'),
    path('editionRegister/', views.editionRegister, name='editionRegister'),
    path('profile/', views.profileUser, name='profile'),
    path('mybooks/', views.mybooks),
    path('book_list/',views.book_list, name='book_list')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)