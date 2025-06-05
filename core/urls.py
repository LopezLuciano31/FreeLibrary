from django.urls import path
from . import views
from .views import loginUserV
from .views import registerUserV
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_complete_form.html'), name='password_reset_complete'),
    
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