from django.db import models

# Create your models here.
class Book(models.Model):
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=1250)
    publicationDate =  models.DateTimeField()
    genres= models.CharField(max_length=50)
    author = models.ForeignKey(Autor)


class Credential(models.Model):
    User = models.CharField(max_length=35)
    passwd =  models.CharField(max_length=35)
    email = models.CharField(max_length=35)

class User(Credential):
    nick = models.CharField(max_length=35)
    joinDate = models.DateTimeField()

 
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
    of = models.ForeignKey(Book)

class Author(models.Model):
    name= models.CharField(max_length=35)
    lastName= models.CharField(max_length=35)
    bio= models.CharField(max_length=1250)
    birth= models.DateTimeField()
    death= models.DateTimeField()
    prof= models.CharField(max_length=35)
    portrait= models.CharField(max_length=100)
