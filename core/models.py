from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Autor(models.Model):
    name= models.CharField(max_length=35)
    lastName= models.CharField(max_length=35)
    bio= models.CharField(max_length=1250)
    birth= models.DateField()
    death= models.DateField(blank=True, null=True)
    prof= models.CharField(max_length=35)
    portrait= models.ImageField(upload_to='img/')

    
class Book(models.Model):
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=1250)
    publicationDate =  models.DateField()
    genres= models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)


    
class Edition(models.Model):
    id= models.IntegerField(primary_key=True)
    title= models.CharField(max_length=70)
    publicationDate=  models.DateField(blank=True, null=True)
    publisher= models.CharField(max_length=70)
    lang= models.CharField(max_length=10)
    pages= models.IntegerField()
    notes= models.CharField(max_length=500)
    place= models.CharField(max_length=70)
    cover=  models.ImageField(upload_to='covers/')
    file= models.FileField(upload_to='books/')
    of = models.ForeignKey(Book, on_delete=models.CASCADE)

class Review(models.Model):
    content= models.CharField(max_length=750)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating =  models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)] )
#cada valor del rango equivale a media estrella, 1 seria media, 2 una, 10 seria cinco estrellas

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Edition, related_name="favorited", blank=True)
    readed = models.ManyToManyField(Edition, related_name="readed", blank=True)
    reading = models.ManyToManyField(Edition, related_name="reading", blank=True)
    