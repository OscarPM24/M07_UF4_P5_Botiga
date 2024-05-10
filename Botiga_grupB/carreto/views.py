from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from .models import Carreto, DetallCarreto
from cataleg.models import Producte
from comandes.models import Comandes
from .serializers import CarretoSerializer, DetallCarretoSerializer
from cataleg.serializers import ProducteSerializer

# Create your views here.
@api_view(['GET'])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def index(request):
    queryset = Carreto.objects.all()
    serializer = CarretoSerializer(queryset, many=True)
    return Response({"Carretons":serializer.data})

@api_view(['GET'])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def carretoActual(request, id):
    queryset = Carreto.objects.get(id=id)
    serializer = CarretoSerializer(queryset)
    return Response({"Carreto":serializer.data})
@api_view(['GET', 'POST'])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def afegeixProducte(request, id):
    carreto = Carreto.objects.get(id=id)
    prod_id = request.data
    if request.method == 'POST':
        producte = Producte.objects.get(id=prod_id)
        if DetallCarreto.objects.filter(producte_id=prod_id):
            detalls = DetallCarreto.objects.get(producte_id=prod_id)
            detalls.quantitat += 1
            detalls.save()
        else:
            carreto.productes.add(producte)
        comanda = Comandes.objects.get(carreto_id=id)
        comanda.total += producte.preu
        comanda.save()
    serializer = CarretoSerializer(carreto)
    return Response({"Carreto": serializer.data})
@api_view(['GET', 'DELETE'])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def eliminaProducte(request, id, producte_id):
    carreto = Carreto.objects.get(id=id)
    if request.method == 'DELETE':
        if DetallCarreto.objects.filter(producte_id=producte_id):
            comanda = Comandes.objects.get(carreto_id=id)
            comanda.total -= Producte.objects.get(id=producte_id).preu
            comanda.save()
            detalls = DetallCarreto.objects.get(producte_id=producte_id)
            if detalls.quantitat > 1:
                detalls.quantitat -= 1
                detalls.save()
            else:
                detalls.delete()
    serializer = CarretoSerializer(carreto)
    return Response({"Carreto": serializer.data})
@api_view(['GET', 'DELETE'])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def eliminaCarreto(request, id):
    carreto = Carreto.objects.get(id=id)
    if request.method == 'DELETE':
        carreto.delete()
    carretons = Carreto.objects.all()
    serializer = CarretoSerializer(carretons, many=True)
    print(serializer)
    return Response({"Carreto": serializer.data})
@api_view(['GET', 'PUT'])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def modificaQuantitat(request, id, producte_id):
    if request.method == 'PUT':
        quantitat = request.data
        if quantitat < 1:
            quantitat = 1
        if DetallCarreto.objects.filter(producte_id=producte_id):
            detalls = DetallCarreto.objects.get(producte_id=producte_id)
            comanda = Comandes.objects.get(carreto_id=id)
            if quantitat < detalls.quantitat:
                comanda.total -= Producte.objects.get(id=producte_id).preu*(detalls.quantitat - quantitat)
            else:
                comanda.total += Producte.objects.get(id=producte_id).preu*(quantitat - detalls.quantitat)
            comanda.save()
            detalls.quantitat = quantitat
            detalls.save()
    detall_product = DetallCarreto.objects.get(producte_id=producte_id)
    serializer = DetallCarretoSerializer(detall_product)
    return Response({"Carreto": serializer.data})