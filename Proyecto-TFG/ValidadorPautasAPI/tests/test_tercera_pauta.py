from django.test import TestCase
from os import path, remove, sep
from ..algorithms import Algorithms

class TestTerceraPauta(TestCase):
    """ 
    Clase Test que comprueba la funcionalidad de la segunda pauta:
        Evitar escribir la hora en formato 24h
    """

    CONCORDANCIA = '-={Concordancia}=-'
    REFERENCIA   = '-={Referencia bibliográfica}=-'
    PATH         = path.dirname(path.abspath(__file__))
    MAX_LINES    = 100

    def setUp(self):
        """ Se crea un fichero txt con los casos prueba formateados """
        remove(f'{self.PATH}{sep}res{sep}NumTlf.txt') if path.exists(f'{self.PATH}{sep}res{sep}NumTlf.txt') else None

        try:
            file_horas    = open(f'{self.PATH}{sep}data{sep}tercera_pauta{sep}ExportacionCORPESHoras.txt', mode='r', encoding='UTF-8')
            file_to_write = open(f'{self.PATH}{sep}res{sep}horas.txt' , mode='w', newline='', encoding='UTF-8')

            is_text, num_lines = False, 0
            for line in file_horas:
                if (num_lines >= self.MAX_LINES): break
                if( self.CONCORDANCIA in line ):
                    is_text = True
                elif( self.REFERENCIA in line ):
                    is_text = False
                elif( is_text and line != '\n' ):
                    file_to_write.write(f'{num_lines}+--+{line}')
                    num_lines += 1

        except IOError as e:
            print(e)
        finally:
            file_horas.close()
            file_to_write.close()

    def get_line(self, test_index):
        text = ""
        try:
            textfile = open(f'{self.PATH}{sep}res{sep}horas.txt', mode='r', encoding='UTF-8')
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
            textfile = open(f'{self.PATH}{sep}res{sep}ResultadosHoras.txt', mode='r', encoding='UTF-8')
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

    def test_tercera_pauta0(self):
        test_index = 0
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta1(self):
        test_index = 1
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta2(self):
        test_index = 2
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta3(self):
        test_index = 3
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta4(self):
        test_index = 4
        text = self.get_line(test_index)

        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_tercera_pauta5(self):
        test_index = 5
        text = self.get_line(test_index)

        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta6(self):
        test_index = 6
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta7(self):
        test_index = 7
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta8(self):
        test_index = 8
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta9(self):
        test_index = 9
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta10(self):
        test_index = 10
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta11(self):
        test_index = 11
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta12(self):
        test_index = 12
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta13(self):
        test_index = 13
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta14(self):
        test_index = 14
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_tercera_pauta15(self):
        test_index = 15
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta16(self):
        test_index = 16
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta17(self):
        test_index = 17
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta18(self):
        test_index = 18
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta19(self):
        test_index = 19
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta20(self):
        test_index = 20
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta21(self):
        test_index = 21
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta22(self):
        test_index = 22
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta23(self):
        test_index = 23
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta24(self):
        test_index = 24
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_tercera_pauta25(self):
        test_index = 25
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta26(self):
        test_index = 26
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta27(self):
        test_index = 27
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta28(self):
        test_index = 28
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta29(self):
        test_index = 29
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta30(self):
        test_index = 30
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta31(self):
        test_index = 31
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta32(self):
        test_index = 32
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta33(self):
        test_index = 33
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta34(self):
        test_index = 34
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_tercera_pauta35(self):
        test_index = 35
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta36(self):
        test_index = 36
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta37(self):
        test_index = 37
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta38(self):
        test_index = 38
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta39(self):
        test_index = 39
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta40(self):
        test_index = 40
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta41(self):
        test_index = 41
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta42(self):
        test_index = 42
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta43(self):
        test_index = 43
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta44(self):
        test_index = 44
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_tercera_pauta45(self):
        test_index = 45
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta46(self):
        test_index = 46
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta47(self):
        test_index = 47
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta48(self):
        test_index = 48
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta49(self):
        test_index = 49
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta50(self):
        test_index = 50
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta51(self):
        test_index = 51
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta52(self):
        test_index = 52
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta53(self):
        test_index = 53
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta54(self):
        test_index = 54
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_tercera_pauta55(self):
        test_index = 55
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta56(self):
        test_index = 56
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta57(self):
        test_index = 57
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta58(self):
        test_index = 58
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta59(self):
        test_index = 59
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta60(self):
        test_index = 60
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta61(self):
        test_index = 61
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta62(self):
        test_index = 62
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta63(self):
        test_index = 63
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta64(self):
        test_index = 64
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_tercera_pauta65(self):
        test_index = 65
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta66(self):
        test_index = 66
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta67(self):
        test_index = 67
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta68(self):
        test_index = 68
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta69(self):
        test_index = 69
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta70(self):
        test_index = 70
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta71(self):
        test_index = 71
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta72(self):
        test_index = 72
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta73(self):
        test_index = 73
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta74(self):
        test_index = 74
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_tercera_pauta75(self):
        test_index = 75
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta76(self):
        test_index = 76
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta77(self):
        test_index = 77
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta78(self):
        test_index = 78
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta79(self):
        test_index = 79
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta80(self):
        test_index = 80
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta81(self):
        test_index = 81
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta82(self):
        test_index = 82
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta83(self):
        test_index = 83
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta84(self):
        test_index = 84
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_tercera_pauta85(self):
        test_index = 85
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta86(self):
        test_index = 86
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta87(self):
        test_index = 87
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta88(self):
        test_index = 88
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta89(self):
        test_index = 89
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta90(self):
        test_index = 90
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta91(self):
        test_index = 91
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta92(self):
        test_index = 92
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta93(self):
        test_index = 93
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta94(self):
        test_index = 94
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)

    def test_tercera_pauta95(self):
        test_index = 95
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta96(self):
        test_index = 96
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta97(self):
        test_index = 97
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta98(self):
        test_index = 98
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
    
    def test_tercera_pauta99(self):
        test_index = 99
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)