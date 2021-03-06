"""
Las vistas de Django que se van a emplear serán vistas basadas en clases.
Esto implica que los metodos vendran bien definidos (cada metodo tendrá 
como nombre el verbo HTTP que implemente) y para que estén bien enrutadas
se hará de la siguiente manera en el archivo urls.py:

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

PRIMERA_PAUTA = 0;
SEGUNDA_PAUTA = 1;
TERCERA_PAUTA = 2;
CUARTA_PAUTA  = 3;

DESCRIPCIONES = [
    "1 - Se debería evitar el uso de palabras de contenido indeterminado",
    "2 - Los numeros de telefono se deberian separar por bloques",
    "3 - Evitar escribir la hora en formato 24h",
    "4 - Evitar el uso de conectores complejos entre oraciones",
]

class ComprobarPrimeraPauta(APIView):
    """ Vista del análisis de la primera pauta """

    def post(self, request):
        """ Petición: POST - Response -> El objeto serializado si ha tenido exito. Error e.o.c """

        try:
            # Aqui es donde podemos tener 'KeyError' si no se pasa el documento como clave en el body de la peticion
            texto = request.data['documento']

            id = hashlib.sha256(texto.encode()).hexdigest()

            algoritmo = Algorithms(texto)
            passed, reason = algoritmo.validador_primera_pauta()
            
            documento  = Documento(id = id, descripcion = DESCRIPCIONES[PRIMERA_PAUTA], passed = passed, reason = reason)
            serializer = DocumentoSerializer(documento)

            return Response(serializer.data, status = status.HTTP_200_OK)

        except KeyError:
            return Response({"error": "No se ha recibido el texto a analizar."}, status = status.HTTP_400_BAD_REQUEST)

class ComprobarSegundaPauta(APIView):
    """ Vista del análisis de la segunda pauta """

    def post(self, request):
        """ Petición: POST - Response -> El objeto serializado si ha tenido exito. Error e.o.c """

        try:
            # Aqui es donde podemos tener 'KeyError' si no se pasa el documento como clave en el body de la peticion
            texto = request.data['documento']
            id = hashlib.sha256(texto.encode()).hexdigest()
            
            algoritmos = Algorithms(texto)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()

            objeto = {
                "id": id,
                "descripcion": DESCRIPCIONES[SEGUNDA_PAUTA],
                "passed": passed,
                "reason": reason,
                "correccion": correccion
            }

            # Se devuelve el objeto en la respuesta. La serializacion es automatica con los objetos de python
            return Response(objeto, status = status.HTTP_200_OK)

        except KeyError:
            return Response({"error": "No se ha recibido el texto a analizar."}, status = status.HTTP_400_BAD_REQUEST)

class ComprobarTerceraPauta(APIView):
    """ Vista del análisis de la tercera pauta. """
    
    def post(self, request):
        """ Petición: POST - Response -> El objeto serializado si ha tenido exito. Error e.o.c """

        try:
            # Aqui es donde podemos tener 'KeyError' si no se pasa el documento como clave en el body de la peticion
            texto = request.data['documento']
            id = hashlib.sha256(texto.encode()).hexdigest()
            
            algoritmos = Algorithms(texto)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            objeto = {
                "id": id,
                "descripcion": DESCRIPCIONES[TERCERA_PAUTA],
                "passed": passed,
                "reason": reason,
                "correccion": correccion
            }

            # Se devuelve el objeto en la respuesta. La serializacion es automatica con los objetos de python
            return Response(objeto, status = status.HTTP_200_OK)

        except KeyError:
            return Response({"error": "No se ha recibido el texto a analizar."}, status = status.HTTP_400_BAD_REQUEST)

class ComprobarCuartaPauta(APIView):
    """ Petición: POST - Response -> El objeto serializado si ha tenido exito. Error e.o.c """

    def post(self, request):

        try:
            # Aqui es donde podemos tener 'KeyError' si no se pasa el documento como clave en el body de la peticion
            texto = request.data['documento']

            id = hashlib.sha256(texto.encode()).hexdigest()

            algoritmos     = Algorithms(texto)
            passed, reason = algoritmos.validador_cuarta_pauta()

            documento  = Documento(id = id, descripcion = DESCRIPCIONES[CUARTA_PAUTA], passed = passed, reason = reason)
            serializer = DocumentoSerializer(documento)

            return Response(serializer.data, status = status.HTTP_200_OK)
        
        except KeyError:
            return Response({"error": "No se ha recibido el texto a analizar."}, status = status.HTTP_400_BAD_REQUEST)