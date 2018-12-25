from django.db import models

# Create your models here.

class Post(models.Model):

    nome=       models.CharField(max_length=200)
    data=       models.DateField()

class Utente(models.Model):

    nome=       models.CharField(max_length=200)
    cognome=    models.CharField(max_length=200)
    foto=       models.ImageField()
    post=       models.ForeignKey(Post,on_delete=models.CASCADE)


