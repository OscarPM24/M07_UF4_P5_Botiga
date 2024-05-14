from rest_framework import serializers
from .models import Comandes
from carreto.serializers import CarretoSerializer

"""
    Serializador per mostrar les dades de les comandes. Aquesta mostra:
        - id usuari
        - carreto
            - mostra les dades del carreto (crida a CarretoSerializer)
        - import total (float)
"""
class ComandesSerializer(serializers.ModelSerializer):
    carreto = CarretoSerializer()
    class Meta:
        model = Comandes
        fields = ['user', 'carreto', 'total']