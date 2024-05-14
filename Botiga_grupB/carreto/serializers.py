from rest_framework import serializers
from .models import Carreto, DetallCarreto
from cataleg.serializers import ProducteSerializer

"""
    Serialitzador de les dades del DetallCarreto per mostrar els seus camps. Aquest crida el serialitzador 
    de Producte per mostrar també els camps de cada producte.
"""
class DetallCarretoSerializer(serializers.ModelSerializer):
    producte = ProducteSerializer()
    class Meta:
        model = DetallCarreto
        fields = ['producte', 'quantitat']

"""
    Serialitzador de les dades del Carreto. Aquest crida directament al serialitzador del DetallCarreto per
    mostrar totes les dades (Carreto -> DetallCarreto -> Producte).
"""
class CarretoSerializer(serializers.ModelSerializer):
    productes = DetallCarretoSerializer(many=True, source='detallcarreto_set')
    class Meta:
        model = Carreto
        fields = ['id', 'productes']