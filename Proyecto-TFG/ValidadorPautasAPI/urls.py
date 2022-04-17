"""
Las URIs para los distintos recursos son:
    - Primera pauta:  /api/comp/cont-indet
    - Segunda pauta:  /api/comp/num-tlf
    - Tercera pauta:  /api/comp/form-hora
    - Cuarta pauta:   /api/comp/conec-comp
    - Quinto recurso: /api/analisis-completo
"""

from django.urls import path
from . import views

urlpatterns = [
    path('comp/cont-indet/', views.ComprobarPrimeraPauta.as_view(), name = 'Contenido Indeterminado'),
    path('comp/num-tlf/', views.ComprobarSegundaPauta.as_view(), name = 'Numero de Telefono'),
    path('comp/form-hora/', views.ComprobarTerceraPauta.as_view(), name = 'Formateo de la Hora'),
    path('comp/conec-comp/', views.ComprobarCuartaPauta.as_view(), name = 'Conectores Complejos'),
    path('analisis-completo/', views.AnalisisCompleto.as_view(), name = 'Analisis Completo'),
]