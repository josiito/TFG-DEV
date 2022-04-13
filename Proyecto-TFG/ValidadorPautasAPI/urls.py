from django.urls import path
from . import views

urlpatterns = [
    path('comp/cont-indet', views.index, name='index'),
]