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
    carreto = Carreto.objects.get(id=id_carreto)  # Agafem el carretó que volem pagar
    serializer = CarretoSerializer(carreto)  # El serialitzem per que es vegi a la pantalla en format JSON
    if carreto.pagat:
        return Response({"message": "Aquest carreto ja està pagat!"})  # Si el carreto està pagat mostrem un missatge dient que ja està pagat

    if request.method == "POST":  # Si el métode de la petició és POST
        dades = request.data  # Agafem les dades de la request
        pagament = Pagaments.objects.filter(tarjeta=dades['tarjeta'])  # Busquem una tarjeta que correspongui amb les dades donades
        if len(pagament) != 0: # Si trobem una tarjeta
            pagament = Pagaments.objects.get(tarjeta=dades['tarjeta'])  # Agafem la tarjeta correcta
            if dades["tarjeta"] == pagament.tarjeta and dades["data_caducitat"] == pagament.data_caducitat and dades["cvc"] == pagament.cvc:  # Comparem si totes les dades (tarjeta, data_caducitat i cvc) corresponen
                carreto.pagat = True  # Paguem el carretó
                carreto.save()  # I el guardem
                return Response({"message": "Pagament Correcte!"})  # Pagament Correcte
        return Response({"message": "Pagament Incorrecte!"})  # Pagament Incorrecte (dades != tarjeta)

    return Response({"Carreto": serializer.data})

