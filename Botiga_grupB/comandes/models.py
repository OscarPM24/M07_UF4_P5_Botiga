from django.db import models
from usuari.models import Usuari
from carreto.models import Carreto

# Create your models here.

class Comandes(models.Model):
    user = models.ForeignKey(Usuari, on_delete=models.CASCADE, default=None)
    carreto = models.ForeignKey(Carreto, on_delete=models.CASCADE, default=None)
    total = models.FloatField(default=0)

