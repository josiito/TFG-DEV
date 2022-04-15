"""
Las vistas de Django que se van a emplear serán vistas basadas en clases.
Esto implica que los metodos vendran bien definidos (cada metodo tendrá 
como nombre el verbo HTTP que implemente) y para que estén bien enrutadas
se hará de la siguiente manera:

>> path('<ruta>/', views.<nombre_vista>.as_view())

De esta manera tendremos un código más limpio, ordenado y escalable.
"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# import hashlib
# import datetime

from .models import Documento
from .serializers import DocumentoSerializer
from .algorithms import Algorithms

DESCRIPCIONES = [
    "1 - Se debería evitar el uso de palabras de contenido indeterminado",
    "2 - Los numeros de telefono se deberian separar por bloques",
    "3 - Se debera escribir la hora en formato 24h",
    "4 - Evitar el uso de conectores complejos entre oraciones",
    "Analisis completo del documento"
]

class ComprobarPrimeraPauta(APIView):
    """
    Clase que se encarga de comprobar si el documento cumple con la primera pauta.
    """

    def get(self, request, format=None):
        """
        Función que se encarga de comprobar si el documento cumple con la primera pauta.
        """

        try:
            texto = request.data['documento']

            # id = int(hashlib.sha256(texto.encode()).hexdigest())
            id = 1
            passed = self.get_first_guideline(texto)

            documento  = Documento(id = id, descripcion = DESCRIPCIONES[0], passed = passed, reason="")
            serializer = DocumentoSerializer(documento)

            if passed:
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                return Response(status = status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"data": request.data, "error": str(e)}, status = status.HTTP_400_BAD_REQUEST)
            #return Response({"error": "No se ha recibido el documento"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get_first_guideline(self, text):
        return True


    # def get(self, request, format=None):
    #     """
    #     Función que se encarga de comprobar si el documento cumple con la primera pauta.
    #     """

    #     # Obtenemos el documento
    #     documento = Documento.objects.get(id=request.GET['id'])
    #     # Obtenemos el serializador
    #     serializer = DocumentoSerializer(documento)
    #     # Comprobamos si el documento cumple con la primera pauta
    #     if serializer.data['primera_pauta']:
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class ComprobarSegundaPauta(APIView):
    """
    Clase que se encarga de comprobar si el documento cumple con la segunda pauta.
    """

    pass

class ComprobarTerceraPauta(APIView):
    """
    Clase que se encarga de comprobar si el documento cumple con la tercera pauta.
    """
    pass

class ComprobarCuartaPauta(APIView):
    """
    Clase que se encarga de comprobar si el documento cumple con la cuarta pauta.
    """
    pass

class AnalisisCompleto(APIView):
    """
    Clase que se encarga de comprobar si el documento cumple con la quinta pauta.
    """
    pass