from rest_framework import serializers
from .models import Carreto, DetallCarreto
from cataleg.serializers import ProducteSerializer

class DetallCarretoSerializer(serializers.ModelSerializer):
    producte = ProducteSerializer()
    class Meta:
        model = DetallCarreto
        fields = ['producte', 'quantitat']
class CarretoSerializer(serializers.ModelSerializer):
    productes = DetallCarretoSerializer(many=True, source='detallcarreto_set')
    class Meta:
        model = Carreto
        fields = ['id', 'productes']