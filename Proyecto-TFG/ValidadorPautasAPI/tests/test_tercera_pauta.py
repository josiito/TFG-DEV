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
    MAX_LINES    = 350

    def setUp(self):
        """ Se crea un fichero txt con los casos prueba formateados """

        try:
            file_horas    = open(f'{self.PATH}{sep}data{sep}tercera_pauta{sep}ExportacionCORPESHoras.txt', mode='r', encoding='UTF-8')
            file_to_write = open(f'{self.PATH}{sep}data{sep}tercera_pauta{sep}ExportacionCORPESHoras-FORMATEADAS.txt' , mode='w', encoding='UTF-8')

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
            textfile = open(f'{self.PATH}{sep}data{sep}tercera_pauta{sep}ExportacionCORPESHoras-FORMATEADAS.txt', mode='r', encoding='UTF-8')
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
            textfile = open(f'{self.PATH}{sep}data{sep}tercera_pauta{sep}ExportacionCORPESHoras-RESULTADOS.txt', mode='r', encoding='UTF-8')
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
        
    def test_tercera_pauta100(self):
        test_index = 100
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta101(self):
        test_index = 101
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta102(self):
        test_index = 102
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta103(self):
        test_index = 103
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta104(self):
        test_index = 104
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta105(self):
        test_index = 105
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta106(self):
        test_index = 106
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta107(self):
        test_index = 107
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta108(self):
        test_index = 108
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta109(self):
        test_index = 109
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta110(self):
        test_index = 110
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta111(self):
        test_index = 111
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta112(self):
        test_index = 112
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta113(self):
        test_index = 113
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta114(self):
        test_index = 114
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta115(self):
        test_index = 115
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta116(self):
        test_index = 116
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta117(self):
        test_index = 117
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta118(self):
        test_index = 118
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta119(self):
        test_index = 119
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta120(self):
        test_index = 120
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta121(self):
        test_index = 121
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta122(self):
        test_index = 122
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta123(self):
        test_index = 123
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta124(self):
        test_index = 124
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta125(self):
        test_index = 125
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta126(self):
        test_index = 126
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta127(self):
        test_index = 127
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta128(self):
        test_index = 128
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta129(self):
        test_index = 129
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta130(self):
        test_index = 130
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta131(self):
        test_index = 131
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta132(self):
        test_index = 132
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta133(self):
        test_index = 133
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta134(self):
        test_index = 134
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta135(self):
        test_index = 135
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta136(self):
        test_index = 136
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta137(self):
        test_index = 137
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta138(self):
        test_index = 138
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta139(self):
        test_index = 139
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta140(self):
        test_index = 140
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta141(self):
        test_index = 141
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta142(self):
        test_index = 142
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta143(self):
        test_index = 143
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta144(self):
        test_index = 144
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta145(self):
        test_index = 145
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta146(self):
        test_index = 146
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta147(self):
        test_index = 147
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta148(self):
        test_index = 148
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta149(self):
        test_index = 149
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta150(self):
        test_index = 150
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta151(self):
        test_index = 151
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta152(self):
        test_index = 152
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta153(self):
        test_index = 153
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta154(self):
        test_index = 154
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta155(self):
        test_index = 155
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta156(self):
        test_index = 156
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta157(self):
        test_index = 157
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta158(self):
        test_index = 158
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta159(self):
        test_index = 159
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta160(self):
        test_index = 160
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta161(self):
        test_index = 161
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta162(self):
        test_index = 162
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta163(self):
        test_index = 163
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta164(self):
        test_index = 164
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta165(self):
        test_index = 165
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta166(self):
        test_index = 166
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta167(self):
        test_index = 167
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta168(self):
        test_index = 168
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta169(self):
        test_index = 169
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta170(self):
        test_index = 170
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta171(self):
        test_index = 171
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta172(self):
        test_index = 172
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta173(self):
        test_index = 173
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta174(self):
        test_index = 174
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta175(self):
        test_index = 175
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta176(self):
        test_index = 176
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta177(self):
        test_index = 177
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta178(self):
        test_index = 178
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta179(self):
        test_index = 179
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta180(self):
        test_index = 180
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta181(self):
        test_index = 181
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta182(self):
        test_index = 182
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta183(self):
        test_index = 183
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta184(self):
        test_index = 184
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta185(self):
        test_index = 185
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta186(self):
        test_index = 186
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta187(self):
        test_index = 187
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta188(self):
        test_index = 188
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta189(self):
        test_index = 189
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta190(self):
        test_index = 190
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta191(self):
        test_index = 191
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta192(self):
        test_index = 192
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta193(self):
        test_index = 193
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta194(self):
        test_index = 194
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta195(self):
        test_index = 195
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta196(self):
        test_index = 196
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta197(self):
        test_index = 197
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta198(self):
        test_index = 198
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta199(self):
        test_index = 199
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta200(self):
        test_index = 200
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta201(self):
        test_index = 201
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta202(self):
        test_index = 202
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta203(self):
        test_index = 203
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta204(self):
        test_index = 204
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta205(self):
        test_index = 205
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta206(self):
        test_index = 206
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta207(self):
        test_index = 207
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta208(self):
        test_index = 208
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta209(self):
        test_index = 209
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta210(self):
        test_index = 210
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta211(self):
        test_index = 211
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta212(self):
        test_index = 212
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta213(self):
        test_index = 213
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta214(self):
        test_index = 214
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta215(self):
        test_index = 215
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta216(self):
        test_index = 216
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta217(self):
        test_index = 217
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta218(self):
        test_index = 218
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta219(self):
        test_index = 219
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta220(self):
        test_index = 220
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta221(self):
        test_index = 221
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta222(self):
        test_index = 222
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta223(self):
        test_index = 223
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta224(self):
        test_index = 224
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta225(self):
        test_index = 225
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta226(self):
        test_index = 226
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta227(self):
        test_index = 227
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta228(self):
        test_index = 228
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta229(self):
        test_index = 229
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta230(self):
        test_index = 230
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta231(self):
        test_index = 231
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta232(self):
        test_index = 232
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta233(self):
        test_index = 233
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta234(self):
        test_index = 234
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta235(self):
        test_index = 235
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta236(self):
        test_index = 236
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta237(self):
        test_index = 237
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta238(self):
        test_index = 238
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta239(self):
        test_index = 239
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta240(self):
        test_index = 240
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta241(self):
        test_index = 241
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta242(self):
        test_index = 242
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta243(self):
        test_index = 243
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta244(self):
        test_index = 244
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta245(self):
        test_index = 245
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta246(self):
        test_index = 246
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta247(self):
        test_index = 247
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta248(self):
        test_index = 248
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta249(self):
        test_index = 249
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta250(self):
        test_index = 250
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta251(self):
        test_index = 251
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta252(self):
        test_index = 252
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta253(self):
        test_index = 253
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta254(self):
        test_index = 254
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta255(self):
        test_index = 255
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta256(self):
        test_index = 256
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta257(self):
        test_index = 257
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta258(self):
        test_index = 258
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta259(self):
        test_index = 259
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta260(self):
        test_index = 260
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta261(self):
        test_index = 261
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta262(self):
        test_index = 262
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta263(self):
        test_index = 263
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta264(self):
        test_index = 264
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta265(self):
        test_index = 265
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta266(self):
        test_index = 266
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta267(self):
        test_index = 267
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta268(self):
        test_index = 268
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta269(self):
        test_index = 269
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta270(self):
        test_index = 270
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta271(self):
        test_index = 271
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta272(self):
        test_index = 272
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta273(self):
        test_index = 273
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta274(self):
        test_index = 274
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta275(self):
        test_index = 275
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta276(self):
        test_index = 276
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta277(self):
        test_index = 277
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta278(self):
        test_index = 278
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta279(self):
        test_index = 279
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta280(self):
        test_index = 280
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta281(self):
        test_index = 281
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta282(self):
        test_index = 282
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta283(self):
        test_index = 283
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta284(self):
        test_index = 284
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta285(self):
        test_index = 285
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta286(self):
        test_index = 286
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta287(self):
        test_index = 287
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta288(self):
        test_index = 288
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta289(self):
        test_index = 289
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta290(self):
        test_index = 290
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta291(self):
        test_index = 291
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta292(self):
        test_index = 292
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta293(self):
        test_index = 293
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta294(self):
        test_index = 294
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta295(self):
        test_index = 295
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta296(self):
        test_index = 296
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta297(self):
        test_index = 297
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta298(self):
        test_index = 298
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta299(self):
        test_index = 299
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta300(self):
        test_index = 300
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta301(self):
        test_index = 301
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta302(self):
        test_index = 302
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta303(self):
        test_index = 303
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta304(self):
        test_index = 304
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta305(self):
        test_index = 305
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta306(self):
        test_index = 306
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta307(self):
        test_index = 307
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta308(self):
        test_index = 308
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta309(self):
        test_index = 309
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta310(self):
        test_index = 310
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta311(self):
        test_index = 311
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta312(self):
        test_index = 312
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta313(self):
        test_index = 313
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta314(self):
        test_index = 314
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta315(self):
        test_index = 315
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta316(self):
        test_index = 316
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta317(self):
        test_index = 317
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta318(self):
        test_index = 318
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta319(self):
        test_index = 319
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta320(self):
        test_index = 320
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta321(self):
        test_index = 321
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta322(self):
        test_index = 322
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta323(self):
        test_index = 323
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta324(self):
        test_index = 324
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta325(self):
        test_index = 325
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta326(self):
        test_index = 326
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta327(self):
        test_index = 327
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta328(self):
        test_index = 328
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta329(self):
        test_index = 329
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta330(self):
        test_index = 330
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta331(self):
        test_index = 331
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta332(self):
        test_index = 332
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta333(self):
        test_index = 333
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta334(self):
        test_index = 334
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta335(self):
        test_index = 335
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta336(self):
        test_index = 336
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta337(self):
        test_index = 337
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta338(self):
        test_index = 338
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta339(self):
        test_index = 339
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta340(self):
        test_index = 340
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta341(self):
        test_index = 341
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta342(self):
        test_index = 342
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta343(self):
        test_index = 343
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta344(self):
        test_index = 344
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta345(self):
        test_index = 345
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta346(self):
        test_index = 346
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta347(self):
        test_index = 347
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta348(self):
        test_index = 348
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        
    def test_tercera_pauta349(self):
        test_index = 349
        text = self.get_line(test_index)
            
        if text:
            algoritmos = Algorithms(text)
            passed, reason, correccion = algoritmos.validador_tercera_pauta()

            passed_txt, reason_txt, correccion_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            self.assertEqual(str(correccion), correccion_txt)
        