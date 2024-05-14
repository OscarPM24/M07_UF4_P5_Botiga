from django.db import models
from usuari.models import Usuari
from carreto.models import Carreto

"""
    Model Comandes ->
        - usuari: associat a una id d'usuari
        - carreto: associat a una id de carreto
        - total: el import total dels productes que conté la comanda
"""
class Comandes(models.Model):
    user = models.ForeignKey(Usuari, on_delete=models.CASCADE, default=None)
    carreto = models.ForeignKey(Carreto, on_delete=models.CASCADE, default=None)
    total = models.FloatField(default=0)

