from django.urls import path
from .views import ( 
    main, info, acerca_de
)

urlpatterns = [
    path('', main, name='index'),
    path('informacion', info, name='info'),
    path('acerca-de', acerca_de, name='acerca-de'),
]