"""
Serializador para serializar y deserializar las instancias
de representaciones JSON.
"""

from rest_framework import serializers
from .models import Documento

class DocumentoSerializer(serializers.ModelSerializer):
    """
    Serializador para la clase Documento.
    """

    # Campos que serializan o desrializan el objeto json
    id          = serializers.IntegerField(read_only=True)
    descripcion = serializers.CharField(max_length=200)
    passed      = serializers.BooleanField(default=False)
    reason      = serializers.CharField(max_length=300, default="")

    class Meta:
        model = Documento
        fields = ('id', 'descripcion', 'passed', 'reason')