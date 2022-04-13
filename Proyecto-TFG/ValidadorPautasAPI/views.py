from .models import Documento
from .serializers import ModelSerializer

from rest_framework import generics

class DocumentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Documento.objects.all()
    serializer_class = ModelSerializer