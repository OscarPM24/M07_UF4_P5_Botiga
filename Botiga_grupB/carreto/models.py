from django.db import models
from cataleg.models import Producte
from usuari.models import Usuari

"""
Model Carreto que conté:
    - usuari: la id d'un usuari
    - productes: una llista de productes associats per DetallCarreto
    - pagat: un boolean que indica si està pagat o no
"""

class Carreto(models.Model):
    usuari = models.ForeignKey(Usuari, null=True, on_delete=models.CASCADE)
    productes = models.ManyToManyField(Producte, through='DetallCarreto')
    pagat = models.BooleanField(default=False)

"""
Model DetallCarreto: model creat per associar un producte a un carreto i la quantitat que hi ha d'aquest.
    Aquest model serveix per després, poder mostrar tots els productes que conté un carreto.
"""
class DetallCarreto(models.Model):
    carreto = models.ForeignKey(Carreto, on_delete=models.CASCADE)
    producte = models.ForeignKey(Producte, on_delete=models.CASCADE)
    quantitat = models.IntegerField(default=1)

