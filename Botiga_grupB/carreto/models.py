from django.db import models
from cataleg.models import Producte
# Create your models here.

class Carreto(models.Model):
    id_producte = models.ForeignKey(Producte, on_delete=models.CASCADE)
