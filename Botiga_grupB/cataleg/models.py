from django.db import models

# Create your models here.
class Producte(models.Model):
    nom = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    preu = models.FloatField(default=0)
    estoc = models.IntegerField(default=0)
    gama = models.CharField(max_length=30)
    pes = models.FloatField(default=0)

class Cataleg(models.Model):
    id_producte = models.ForeignKey(Producte, on_delete=models.CASCADE)