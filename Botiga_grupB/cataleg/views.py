from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from .models import Producte, Cataleg
from .serializers import ProducteSerializer, CatalegSerializer

@api_view(["GET", "POST"])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(["GET"])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def catalegs(request):
    queryset = Cataleg.objects.all()
    serializer = CatalegSerializer(queryset, many=True)
    return Response({"Catalegs": serializer.data})

@api_view(["GET"])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def cataleg(request, id):
    queryset = Cataleg.objects.get(id=id)
    serializer = CatalegSerializer(queryset)
    return Response({"Cataleg": serializer.data})

@api_view(["GET", "POST"])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def afegirProducte(request, id):
    queryset = Cataleg.objects.get(id=id)
    if request.method == "POST":
        producte = request.data
        queryset.productes.add(producte)

    queryset = Cataleg.objects.get(id=id)
    serializer = CatalegSerializer(queryset)
    return Response({"Cataleg": serializer.data})

@api_view(["GET", "DELETE"])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def eliminarProducte(request, id_cataleg, id_prod):
    queryset = Cataleg.objects.get(id=id_cataleg)
    if request.method == "DELETE":
        queryset.productes.remove(id_prod)

    queryset = Cataleg.objects.get(id=id_cataleg)
    serializer = CatalegSerializer(queryset)
    return Response({"Cataleg": serializer.data})

@api_view(["GET", "PUT"])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def editarProducte(request, id_cataleg, id_prod):
    print("editando")
    queryset = Cataleg.objects.get(id=id_cataleg)
    if request.method == "PUT":
        dades = request.data
        producte = Producte.objects.get(id=id_prod)
        for key, value in dades.items():
            setattr(producte, key, value)
        producte.save()

    queryset = Cataleg.objects.get(id=id_cataleg)
    serializer = CatalegSerializer(queryset)
    return Response({"Cataleg": serializer.data})