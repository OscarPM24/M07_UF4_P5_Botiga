from rest_framework import serializers
from .models import Producte, Cataleg

class ProducteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producte
        fields = ['id', 'nom', 'marca', 'gama', 'preu', 'estoc', 'pes']

class CatalegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cataleg
        fields = ['id', 'productes']