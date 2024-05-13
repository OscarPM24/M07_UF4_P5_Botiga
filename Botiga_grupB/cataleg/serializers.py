from rest_framework import serializers
from .models import Producte, Cataleg

# Serialitzador dels Productes, per que es vegin bé en el rest-framework
class ProducteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producte
        fields = ['id', 'nom', 'marca', 'gama', 'preu', 'estoc', 'pes']


# Serialitzador dels Catàlegs, per que es vegin bé en el rest-framework
class CatalegSerializer(serializers.ModelSerializer):
    productes = ProducteSerializer(many="True")
    class Meta:
        model = Cataleg
        fields = ['id', 'productes']