from django.test import TestCase
from os import path, remove
# from ..algorithms import Algorithms

import csv

class TestPrimeraPauta(TestCase):

    CONCORDANCIA = '-={Concordancia}=-'
    REFERENCIA   = '-={Referencia bibliográfica}=-'
    PATH         = path.dirname(path.abspath(__file__))

    def setUp(self):
        """ Crea un archivo csv a partir de un archivo txt antes de empezar los tests """
        remove(f'{self.PATH}/data/horas.csv') if path.exists(f'{self.PATH}/data/horas.csv') else None

        with open(f'{self.PATH}/data/ExportacionCORPESHoras.txt', mode='r', encoding='UTF-8') as file:
            with open(f'{self.PATH}/data/horas.csv', mode='w', newline='', encoding='UTF-8') as csvfile:
                isText, i = False, 0
                writer = csv.DictWriter(csvfile, fieldnames=['Prueba', 'Texto'], delimiter=';')

                for line in file.readlines():
                    if( self.CONCORDANCIA in line ):
                        isText = True
                    if( isText ):
                        writer.writerow({ 'Prueba': i, 'Texto': ["a", "b", "c"] })
                        i += 1
                    if( self.REFERENCIA in line ):
                        isText = False

    def tearDown(self):
        """ Elimina un archivo csv despues de hacer todos los tests """
        remove(f'{self.PATH}/data/horas.csv') if path.exists(f'{self.PATH}/data/horas.csv') else None

    def test_primera_pauta0(self):
        """ Test de la primera pauta: Se debería evitar el uso de palabras de contenido indeterminado """
        # algoritmos = Algorithms('Hay algo que quiero decirte')
        self.assertEqual(1, 1)