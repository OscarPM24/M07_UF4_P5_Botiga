from django.db import models
from cataleg.models import Producte
from usuari.models import Usuari
# Create your models here.

class Carreto(models.Model):
    usuari = models.ForeignKey(Usuari, null=True, on_delete=models.CASCADE)
    productes = models.ManyToManyField(Producte, through='DetallCarreto')

class DetallCarreto(models.Model):
    carreto = models.ForeignKey(Carreto, on_delete=models.CASCADE)
    producte = models.ForeignKey(Producte, on_delete=models.CASCADE)
    quantitat = models.IntegerField(default=1)