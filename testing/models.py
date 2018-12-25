from django.db import models

# Create your models here.
class Utente(models.Model):

    nome=     models.CharField(max_length=200)
    cognome=  models.CharField(max_length=200)
    foto=     models.ImageField()
