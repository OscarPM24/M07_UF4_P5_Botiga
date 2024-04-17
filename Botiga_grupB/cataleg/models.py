from django.db import models

# Create your models here.
class Producte(models.Model):
    nom = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    preu = models.FloatField()
    estoc = models.IntegerField()
    gama = models.CharField(max_length=30)
    pes = models.FloatField()

class Cataleg(models.Model):
    id_producte = models.ForeignKey(Producte, on_delete=models.CASCADE)