from rest_framework.decorators import api_view, renderer_classes
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


