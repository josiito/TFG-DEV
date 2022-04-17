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

import hashlib

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
    """ Vista del análisis de la primera pauta """

    def get(self, request):
        """ Petición: GET - Response -> El objeto serializado si ha tenido exito. Error e.o.c """

        try:
            texto = request.data['documento']

            id = hashlib.sha256(texto.encode()).hexdigest()
            
            algoritmo = Algorithms(texto)
            passed, reason = algoritmo.validador_primera_pauta()

            documento  = Documento(id = id, descripcion = DESCRIPCIONES[0], passed = passed, reason = reason)
            serializer = DocumentoSerializer(documento)

            return Response(serializer.data, status = status.HTTP_200_OK)

        except KeyError as e:
            return Response({"error": "No se ha recibido el texto a analizar."}, status = status.HTTP_400_BAD_REQUEST)

class ComprobarSegundaPauta(APIView):
    """ Vista del análisis de la segunda pauta """

    def get(self, request):
        """ Petición: GET - Response -> El objeto serializado si ha tenido exito. Error e.o.c """

        try:
            texto = request.data['documento']

            id = hashlib.sha256(texto.encode()).hexdigest()

            algoritmos = Algorithms(texto)
            passed, reason, sol_propuesta = algoritmos.validador_segunda_pauta()

            documento  = Documento(id = id, descripcion = DESCRIPCIONES[1], passed = passed, reason = reason)
            serializer = DocumentoSerializer(documento)

            return Response(serializer.data, status = status.HTTP_200_OK)

        except KeyError as e:
            return Response({"error": "No se ha recibido el texto a analizar."}, status = status.HTTP_400_BAD_REQUEST)

class ComprobarTerceraPauta(APIView):
    """ Vista del análisis de la tercera pauta. """
    
    def get(self, request):
        """ Petición: GET - Response -> El objeto serializado si ha tenido exito. Error e.o.c """

        try:
            texto = request.data['documento']

            id = hashlib.sha256(texto.encode()).hexdigest()

            algoritmos     = Algorithms(texto)
            passed, reason = algoritmos.validador_tercera_pauta()

            documento  = Documento(id = id, descripcion = DESCRIPCIONES[2], passed = passed, reason = reason)
            serializer = DocumentoSerializer(documento)

            return Response(serializer.data, status = status.HTTP_200_OK)

        except KeyError as e:
            return Response({"error": "No se ha recibido el texto a analizar."}, status = status.HTTP_400_BAD_REQUEST)

class ComprobarCuartaPauta(APIView):
    """ Vista del análisis de la tercera pauta """

    def get(self, request):

        try:
            texto = request.data['documento']

            id = hashlib.sha256(texto.encode()).hexdigest()

            algoritmos     = Algorithms(texto)
            passed, reason = algoritmos.validador_cuarta_pauta()

            documento  = Documento(id = id, descripcion = DESCRIPCIONES[3], passed = passed, reason = reason)
            serializer = DocumentoSerializer(documento)

            return Response(serializer.data, status = status.HTTP_200_OK)
        
        except KeyError:
            return Response({"error": "No se ha recibido el texto a analizar."}, status = status.HTTP_400_BAD_REQUEST)

    pass

class AnalisisCompleto(APIView):
    """ Vista del análisis completo del documento """
    pass