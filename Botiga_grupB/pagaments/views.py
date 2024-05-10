from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from carreto.models import Carreto
from carreto.serializers import CarretoSerializer
from pagaments.models import Pagaments

# Create your views here.
@api_view(["GET", "POST"])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def pagarCarreto(request, id_carreto):
    carreto = Carreto.objects.get(id=id_carreto)
    serializer = CarretoSerializer(carreto)
    if carreto.pagat:
        return Response({"message": "Aquest carreto ja està pagat!"})

    if request.method == "POST":
        dades = request.data
        pagament = Pagaments.objects.filter(tarjeta=dades['tarjeta'])
        if len(pagament) != 0:
            pagament = Pagaments.objects.get(tarjeta=dades['tarjeta'])
            if dades["tarjeta"] == pagament.tarjeta and dades["data_caducitat"] == pagament.data_caducitat and dades["cvc"] == pagament.cvc:
                carreto.pagat = True
                carreto.save()
                return Response({"message": "Pagament Correcte!"})
        return Response({"message": "Pagament Incorrecte!"})

    return Response({"Carreto": serializer.data})

