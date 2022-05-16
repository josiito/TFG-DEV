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

    # Las razones sera una lista.
    reason = serializers.ListField()

    # Tendrá todos los mismos campos que su modelo
    class Meta:
        model = Documento
        fields = ('id', 'descripcion', 'passed', 'reason')