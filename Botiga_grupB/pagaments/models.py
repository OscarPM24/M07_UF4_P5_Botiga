from django.db import models
from usuari.models import Usuari

# Model dels pagaments.
# Els pagaments tenen tarjeta, data de caducitat, cvc, i un usuari relacionat mitjançant una OneToOne.
class Pagaments(models.Model):
    tarjeta = models.CharField(max_length=30)
    data_caducitat = models.CharField(max_length=30)
    cvc = models.IntegerField(default=0)
    user = models.OneToOneField(Usuari, on_delete=models.CASCADE)