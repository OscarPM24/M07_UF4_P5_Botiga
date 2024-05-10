from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from .models import Comandes
from .serializers import ComandesSerializer
from usuari.models import Usuari

# Create your views here.
@api_view(['GET'])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def historic(request, id):
    comandesSerialitzades = []
    usuari = Usuari.objects.get(id=id)
    comandes = Comandes.objects.filter(user=usuari)
    for comanda in comandes:
        if comanda.carreto.pagat:
            serializer = ComandesSerializer(comanda)
            comandesSerialitzades.append(serializer.data)
    return Response({"Comandes": comandesSerialitzades})

# Create your views here.
@api_view(['GET'])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def pendents(request):
    comandes = Comandes.objects.all()
    comandesPendents = []
    for comanda in comandes:
        if comanda.carreto.pagat == False:
            comandesPendents.append((ComandesSerializer(comanda).data))
    return Response({"Comandes pendents": comandesPendents})
