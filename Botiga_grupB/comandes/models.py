from django.db import models

# Create your models here.
class Comandes(models.Model):
    """
        comandes/historic -> mostra l'historial de compres realitzades
        comandes/pendents -> mostra els carretons sense pagar
    """
