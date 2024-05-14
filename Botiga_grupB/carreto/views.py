#Imports
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from .models import Carreto, DetallCarreto
from cataleg.models import Producte
from comandes.models import Comandes
from .serializers import CarretoSerializer, DetallCarretoSerializer

#Vistes.
#Index function -> agafa tots els carretons de la nostra taula carreto, els serialitza i els retorna com a Response
@api_view(['GET']) #Decorador api_view el qual ens permet agafar els mètodes HTTPS que s'espera en la nostra view
@renderer_classes([BrowsableAPIRenderer, JSONRenderer]) #Renderitzador que ens permet retornar respostes en diferents formats
def index(request):
    queryset = Carreto.objects.all() #Retorna totes les dades de la taula Carreto
    serializer = CarretoSerializer(queryset, many=True) #Serialitza el queryset. Li indiquem 'many=True' perquè hi ha més d'un objecte.
    return Response({"Carretons":serializer.data})

#carretoActual -> View que rep la ID del carreto per paràmetre GET i amb el que ho consulta a la BD (where id=id).
#Un cop rebut l'objecte, el serialitza i retorna la data com a response.
@api_view(['GET'])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def carretoActual(request, id):
    queryset = Carreto.objects.get(id=id)
    serializer = CarretoSerializer(queryset)
    return Response({"Carreto":serializer.data})

#afegeixProducte -> Selecciona el carreto amb la ID que rep per mètode GET i amb les dades pasades per POST(id producte)
#afegirà el producte al carreto. Abans de fer-ho, comprova si ja existeix en el detall i si és així, afegirà +1 a la
#quantitat del producte existent.
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
#eliminaProducte -> Rep la id del carreto actual a esborrar el producte i la id del producte que volem eliminar els quals
#els indiquem per mètode GET. Un cop això, fem servir el mètode DELETE per esborrar el producte del carreto. Si la quantitat
#d'aquest és superior a 1, no l'eminarà, però li restarà 1.
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
#eliminaCarreto -> Rep per mètode GET la id del carreto i l'esborra completament. Després retorna els carretons que
#existeixen.
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
#modificaQuantitat -> Rep la id del carreto i la id del producte a modificar per mètode GET. Cerca el producte per id
#i modifica la quantitat amb la request.data que rep per mètode PUT. Actualitzem les dades amb .save()
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