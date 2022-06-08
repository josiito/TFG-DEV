from django.test import TestCase
from os import path, remove
from ..algorithms import Algorithms

class TestSegundaPauta(TestCase):
    """ 
    Clase Test que comprueba la funcionalidad de la segunda pauta:
        Los numeros de telefono se deberian separar por bloques
    """

    PATH = path.dirname(path.abspath(__file__))

    def setUp(self):
        """ Se crea un fichero txt con los casos prueba formateados """
        remove(f'{self.PATH}/res/NumTlf.txt') if path.exists(f'{self.PATH}/res/NumTlf.txt') else None

        with open(f'{self.PATH}/data/ExportacionEjemplosNumTelefono.txt', mode='r', encoding='UTF-8') as file_asunto:
            with open(f'{self.PATH}/res/NumTlf.txt', mode='w', newline='', encoding='UTF-8') as textfile:
                i = 0
                for line in file_asunto:
                    textfile.write(f'{i}+--+{line}')
                    i += 1

    def get_line(self, test_index):
        text = ""
        try:
            textfile = open(f'{self.PATH}/res/NumTlf.txt', mode='r', encoding='UTF-8')
            for line in textfile:
                splitter = line.split('+--+')
                if int(splitter[0]) == test_index:
                    text = splitter[1]
                    break
            
            # Devuelve la linea o un str vacio si no la encontrase
            return text

        except IOError as e:
            print(e)
        finally:
            textfile.close()

    def get_correct_line(self, test_index):
        passed, reason, correction = False, [], []
        try:
            textfile = open(f'{self.PATH}/res/NumerosTelefono.txt', mode='r', encoding='UTF-8')
            for line in textfile:
                splitter = line.split(';')
                if int(splitter[0]) == test_index:
                    passed = splitter[1]
                    reason = splitter[2]
                    correction = splitter[3].replace('\n', '')
                    break
            
            return passed, reason, correction

        except IOError as e:
            print(e)
        finally:
            textfile.close()

    def test_segunda_pauta0(self):
        test_index = 0
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_segunda_pauta1(self):
        test_index = 1
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta2(self):
        test_index = 2
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta3(self):
        test_index = 3
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta4(self):
        test_index = 4
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_segunda_pauta5(self):
        test_index = 5
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta6(self):
        test_index = 6
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_segunda_pauta7(self):
        test_index = 7
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta8(self):
        test_index = 8
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta9(self):
        test_index = 9
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta10(self):
        test_index = 10
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta11(self):
        test_index = 11
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta12(self):
        test_index = 12
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta13(self):
        test_index = 13
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_segunda_pauta14(self):
        test_index = 14
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta15(self):
        test_index = 15
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta16(self):
        test_index = 16
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta17(self):
        test_index = 17
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta18(self):
        test_index = 18
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta19(self):
        test_index = 19
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta20(self):
        test_index = 20
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta21(self):
        test_index = 21
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta22(self):
        test_index = 22
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_segunda_pauta23(self):
        test_index = 23
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta24(self):
        test_index = 24
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta25(self):
        test_index = 25
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_segunda_pauta26(self):
        test_index = 26
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_segunda_pauta27(self):
        test_index = 27
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta28(self):
        test_index = 28
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta29(self):
        test_index = 29
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta30(self):
        test_index = 30
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta31(self):
        test_index = 31
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta32(self):
        test_index = 32
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_segunda_pauta33(self):
        test_index = 33
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta34(self):
        test_index = 34
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta35(self):
        test_index = 35
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta36(self):
        test_index = 36
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta37(self):
        test_index = 37
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta38(self):
        test_index = 38
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_segunda_pauta39(self):
        test_index = 39
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_segunda_pauta()
            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)