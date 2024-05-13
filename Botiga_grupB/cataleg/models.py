from django.db import models

# Model del producte.
# Els productes tenen nom, marca, preu, estoc, gama i pes
class Producte(models.Model):
    nom = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    preu = models.FloatField(default=0)
    estoc = models.IntegerField(default=0)
    gama = models.CharField(max_length=30)
    pes = models.FloatField(default=0)

# Model del catàleg
# Els catàlegs tenen productes, en una relació ManyToMany
class Cataleg(models.Model):
    productes = models.ManyToManyField(Producte)
