from rest_framework import serializers
from .models import Comandes
from carreto.serializers import CarretoSerializer

class ComandesSerializer(serializers.ModelSerializer):
    carreto = CarretoSerializer()
    class Meta:
        model = Comandes
        fields = ['user', 'carreto', 'total']