from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from .models import Producte, Cataleg
from .serializers import ProducteSerializer, CatalegSerializer

# View de prova hello
@api_view(["GET", "POST"])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def hello_world(request):
    return Response({"message": "Hello, world!"})

# View de tots els catàlegs
@api_view(["GET"])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def catalegs(request):
    queryset = Cataleg.objects.all()  # Agafem tots els catàlegs de la bd
    serializer = CatalegSerializer(queryset, many=True)  # Serialitzem els catàlegs i indiquem que hi pot haber més d'un amb many=True
    return Response({"Catalegs": serializer.data})

# View que mostra un catàleg (ID per paràmetre)
@api_view(["GET"])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def cataleg(request, id):
    queryset = Cataleg.objects.get(id=id)  # Agafem el catàleg amb la ID passada per paràmetra
    serializer = CatalegSerializer(queryset) # Serialitzem el catàleg
    return Response({"Cataleg": serializer.data})

# View que permet afegir productes a un catàleg (ID per paràmetre)
@api_view(["GET", "POST"])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def afegirProducte(request, id):
    queryset = Cataleg.objects.get(id=id) # Agafem el catàleg amb la ID passada per parámetre
    if request.method == "POST":  # Si el mètode de la petició es POST
        producte = request.data  # Agafem les dades de la petició
        queryset.productes.add(producte)  # Afegim el producte al catàleg

    queryset = Cataleg.objects.get(id=id)  # Tornem a agafar el catàég
    serializer = CatalegSerializer(queryset)  # El serialitzem
    return Response({"Cataleg": serializer.data})

# View que permet eliminar productes d'un catàleg (ID de catàleg i de producte a eliminar par parámetre)
@api_view(["GET", "DELETE"])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def eliminarProducte(request, id_cataleg, id_prod):
    queryset = Cataleg.objects.get(id=id_cataleg)  # Agafem el catàleg amb la ID passada per paràmetre
    if request.method == "DELETE":  # Si el mètode de la petició es DELETE
        queryset.productes.remove(id_prod)  # Eliminem el producte amb la ID passada per paràmetre

    queryset = Cataleg.objects.get(id=id_cataleg)  # Tornem a agafar el catàleg
    serializer = CatalegSerializer(queryset)  # El serialitzem
    return Response({"Cataleg": serializer.data})

# View que permet editar camps d'un producte d'un catàleg (ID de catàleg i de producte a editar per paràmetre)
@api_view(["GET", "PUT"])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def editarProducte(request, id_cataleg, id_prod):
    print("editando")
    queryset = Cataleg.objects.get(id=id_cataleg)  # Agafem el catàleg amb ID passat per paràmetre
    if request.method == "PUT":  # Si el mètode de la petició es PUT
        dades = request.data  # Agafem les dades de la petició
        producte = Producte.objects.get(id=id_prod)  # Obtenim el producte amb la ID corresponent
        for key, value in dades.items():
            setattr(producte, key, value)  # Modifiquem l'atribut del producte amb el valor nou
        producte.save()  # Finalment el guardem a la bd

    queryset = Cataleg.objects.get(id=id_cataleg) # Tornem a agafar el catàleg
    serializer = CatalegSerializer(queryset) # El serialitzem
    return Response({"Cataleg": serializer.data})