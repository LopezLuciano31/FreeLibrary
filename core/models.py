from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Autor(models.Model):
    name= models.CharField(max_length=35)
    lastName= models.CharField(max_length=35)
    bio= models.CharField(max_length=1250)
    birth= models.DateTimeField()
    death= models.DateTimeField()
    prof= models.CharField(max_length=35)
    portrait= models.CharField(max_length=100)

class Book(models.Model):
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=1250)
    publicationDate =  models.DateTimeField()
    genres= models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)


class Edition(models.Model):
    id= models.IntegerField(primary_key=True)
    title= models.CharField(max_length=70)
    publicationDate=  models.DateTimeField()
    publisher= models.CharField(max_length=70)
    lang= models.CharField(max_length=10)
    pages= models.IntegerField()
    notes= models.CharField(max_length=500)
    place= models.CharField(max_length=70)
    cover= models.CharField(max_length=100)
    file= models.CharField(max_length=100)
    of = models.ForeignKey(Book, on_delete=models.CASCADE)

# el modelo 'Profile' se utilizara en remplazo del usuario consumidor,
# los campos nuevos deben insertarse en esta clase,
# ya que el modelo 'User' de Django ya realiza las funciones de autenticacion
# y posee los campos 'email', 'username', 'password', y mas:
# Fuente:
# https://docs.djangoproject.com/en/5.2/topics/auth/default/#user-objects
#
# por lo que unicamente se extiende en los campos que hacen falta.
# Fuente:
# https://docs.djangoproject.com/en/5.2/topics/auth/customizing/#extending-the-existing-user-model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    joinDate = models.DateTimeField()
