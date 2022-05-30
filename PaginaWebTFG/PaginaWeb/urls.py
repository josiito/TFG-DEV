from django.urls import path
from .views import ( 
    main, info, acerca_de, resultado
)

urlpatterns = [
    path('', main, name='index'),
    path('informacion/', info, name='info'),
    path('acerca-de/', acerca_de, name='acerca-de'),
    path('resultado/', resultado, name='resultado'),
]