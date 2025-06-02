from django.db import models


# Create your models here.
class Autor(models.Model):
    name= models.CharField(max_length=35)
    lastName= models.CharField(max_length=35)
    bio= models.CharField(max_length=1250)
    birth= models.DateTimeField()
    death= models.DateTimeField()
    prof= models.CharField(max_length=35)
    portrait= models.ImageField(upload_to='img/')

    
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
    cover=  models.ImageField(upload_to='covers/')
    file= models.FileField(upload_to='books/')
    of = models.ForeignKey(Book, on_delete=models.CASCADE)

