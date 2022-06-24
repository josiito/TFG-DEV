from django.test import TestCase
from os import ( path, sep )
from ..algorithms import Algorithms

class TestCuartaPauta(TestCase):
    """ 
    Clase Test que comprueba la funcionalidad de la segunda pauta:
        Evitar el uso de conectores complejos entre oraciones
    """

    CONCORDANCIA = '-={Concordancia}=-'
    REFERENCIA   = '-={Referencia bibliográfica}=-'
    PATH         = path.dirname(path.abspath(__file__))

    MAX_LINES    = 300

    def setUp(self):
        """ 
        Paso antes de iniciar todas las pruebas: 
            Se crea un fichero txt con los casos prueba formateados
        """
        try: 
            file_conect_ordenacion    = open(f'{self.PATH}{sep}data{sep}cuarta_pauta{sep}ExportacionCORPES-conect-ordenacion(1).txt', mode='r', encoding='UTF-8')
            file_conect_recapilutivos = open(f'{self.PATH}{sep}data{sep}cuarta_pauta{sep}ExportacionCORPES-conect-recapilutivos(2).txt', mode='r', encoding='UTF-8')
            file_conect_consecutivo   = open(f'{self.PATH}{sep}data{sep}cuarta_pauta{sep}ExportacionCORPES-conect-consecutivos(3).txt', mode='r', encoding='UTF-8')
            file_conect_adversativo   = open(f'{self.PATH}{sep}data{sep}cuarta_pauta{sep}ExportacionCORPES-conect-adversativo(4).txt', mode='r', encoding='UTF-8')
            file_to_write             = open(f'{self.PATH}{sep}data{sep}cuarta_pauta{sep}EsportacionCORPESConectores.txt', mode='w', newline='', encoding='UTF-8')
            
            files_to_read = [
                file_conect_adversativo,
                file_conect_consecutivo,
                file_conect_recapilutivos,
                file_conect_ordenacion,
            ]
            # Se escogen los 300 primeros casos de prueba de cada fichero
            index_of_total_line = 0
            for i in range(0, len(files_to_read)):
                is_text, num_lines = False, 0
                for line in files_to_read[i]:
                    if (num_lines >= self.MAX_LINES):
                        break
                    if( self.CONCORDANCIA in line ):
                        is_text = True
                    elif( self.REFERENCIA in line ):
                        is_text = False
                    elif( is_text and line != '\n' ):
                        file_to_write.write(f'{index_of_total_line}+--+{line}')
                        index_of_total_line += 1
                        num_lines += 1

        except IOError as e:
            print(e)
        finally:
            file_conect_adversativo.close()
            file_conect_consecutivo.close()
            file_conect_recapilutivos.close()
            file_conect_ordenacion.close()
            file_to_write.close()

    def get_line(self, test_index):
        text = ""
        try:
            textfile = open(f'{self.PATH}{sep}data{sep}cuarta_pauta{sep}EsportacionCORPESConectores.txt', mode='r', encoding='UTF-8')
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
        passed, reason = False, []
        try:
            textfile = open(f'{self.PATH}{sep}data{sep}cuarta_pauta{sep}EsportacionCORPESConectores-RESULTADOS.txt', mode='r', encoding='UTF-8')
            for line in textfile:
                splitter = line.split(';')
                if int(splitter[0]) == test_index:
                    passed = splitter[1]
                    reason = splitter[2].replace('\n', '')
                    break
            
            return passed, reason

        except IOError as e:
            print(e)
        finally:
            textfile.close()

    def test_cuarta_pauta0(self):
        test_index = 0
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta1(self):
        test_index = 1
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta2(self):
        test_index = 2
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta3(self):
        test_index = 3
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta4(self):
        test_index = 4
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta5(self):
        test_index = 5
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta6(self):
        test_index = 6
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta7(self):
        test_index = 7
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta8(self):
        test_index = 8
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta9(self):
        test_index = 9
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta10(self):
        test_index = 10
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta11(self):
        test_index = 11
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta12(self):
        test_index = 12
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta13(self):
        test_index = 13
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta14(self):
        test_index = 14
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta15(self):
        test_index = 15
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta16(self):
        test_index = 16
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta17(self):
        test_index = 17
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta18(self):
        test_index = 18
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta19(self):
        test_index = 19
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta20(self):
        test_index = 20
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta21(self):
        test_index = 21
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta22(self):
        test_index = 22
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta23(self):
        test_index = 23
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta24(self):
        test_index = 24
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta25(self):
        test_index = 25
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta26(self):
        test_index = 26
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta27(self):
        test_index = 27
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta28(self):
        test_index = 28
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta29(self):
        test_index = 29
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta30(self):
        test_index = 30
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta31(self):
        test_index = 31
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta32(self):
        test_index = 32
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta33(self):
        test_index = 33
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta34(self):
        test_index = 34
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta35(self):
        test_index = 35
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta36(self):
        test_index = 36
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta37(self):
        test_index = 37
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta38(self):
        test_index = 38
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta39(self):
        test_index = 39
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta40(self):
        test_index = 40
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta41(self):
        test_index = 41
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta42(self):
        test_index = 42
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta43(self):
        test_index = 43
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta44(self):
        test_index = 44
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta54(self):
        test_index = 45
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta46(self):
        test_index = 46
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta47(self):
        test_index = 47
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta48(self):
        test_index = 48
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta49(self):
        test_index = 49
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta50(self):
        test_index = 50
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta51(self):
        test_index = 51
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta52(self):
        test_index = 52
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta53(self):
        test_index = 53
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta54(self):
        test_index = 54
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta55(self):
        test_index = 55
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta56(self):
        test_index = 56
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta57(self):
        test_index = 57
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta58(self):
        test_index = 58
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta59(self):
        test_index = 59
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta60(self):
        test_index = 60
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta61(self):
        test_index = 61
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta62(self):
        test_index = 62
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta63(self):
        test_index = 63
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta64(self):
        test_index = 64
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta65(self):
        test_index = 65
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta66(self):
        test_index = 66
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta67(self):
        test_index = 67
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta68(self):
        test_index = 68
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta69(self):
        test_index = 69
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta70(self):
        test_index = 70
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta71(self):
        test_index = 71
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta72(self):
        test_index = 72
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta73(self):
        test_index = 73
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta74(self):
        test_index = 74
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta75(self):
        test_index = 75
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta76(self):
        test_index = 76
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta77(self):
        test_index = 77
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta78(self):
        test_index = 78
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta79(self):
        test_index = 79
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta80(self):
        test_index = 80
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta81(self):
        test_index = 81
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta82(self):
        test_index = 82
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta83(self):
        test_index = 83
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta84(self):
        test_index = 84
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta85(self):
        test_index = 85
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta86(self):
        test_index = 86
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta87(self):
        test_index = 87
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta88(self):
        test_index = 88
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta89(self):
        test_index = 89
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta90(self):
        test_index = 90
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta91(self):
        test_index = 91
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta92(self):
        test_index = 92
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta93(self):
        test_index = 93
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta94(self):
        test_index = 94
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta95(self):
        test_index = 95
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta96(self):
        test_index = 96
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta97(self):
        test_index = 97
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta98(self):
        test_index = 98
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta99(self):
        test_index = 99
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta100(self):
        test_index = 100
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta101(self):
        test_index = 101
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta102(self):
        test_index = 102
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta103(self):
        test_index = 103
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta104(self):
        test_index = 104
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta105(self):
        test_index = 105
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta106(self):
        test_index = 106
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta107(self):
        test_index = 107
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta108(self):
        test_index = 108
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta109(self):
        test_index = 109
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta110(self):
        test_index = 110
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta111(self):
        test_index = 111
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta112(self):
        test_index = 112
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta113(self):
        test_index = 113
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta114(self):
        test_index = 114
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta115(self):
        test_index = 115
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta116(self):
        test_index = 116
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta117(self):
        test_index = 117
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta118(self):
        test_index = 118
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta119(self):
        test_index = 119
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta120(self):
        test_index = 120
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta121(self):
        test_index = 121
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta122(self):
        test_index = 122
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta123(self):
        test_index = 123
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta124(self):
        test_index = 124
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta125(self):
        test_index = 125
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta126(self):
        test_index = 126
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta127(self):
        test_index = 127
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta128(self):
        test_index = 128
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta129(self):
        test_index = 129
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta130(self):
        test_index = 130
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta131(self):
        test_index = 131
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta132(self):
        test_index = 132
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta133(self):
        test_index = 133
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta134(self):
        test_index = 134
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta135(self):
        test_index = 135
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta136(self):
        test_index = 136
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta137(self):
        test_index = 137
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta138(self):
        test_index = 138
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta139(self):
        test_index = 139
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta140(self):
        test_index = 140
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta141(self):
        test_index = 141
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta142(self):
        test_index = 142
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta143(self):
        test_index = 143
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta144(self):
        test_index = 144
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta145(self):
        test_index = 145
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta146(self):
        test_index = 146
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta147(self):
        test_index = 147
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta148(self):
        test_index = 148
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta149(self):
        test_index = 149
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta150(self):
        test_index = 150
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta151(self):
        test_index = 151
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta152(self):
        test_index = 152
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta153(self):
        test_index = 153
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta154(self):
        test_index = 154
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta155(self):
        test_index = 155
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta156(self):
        test_index = 156
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta157(self):
        test_index = 157
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta158(self):
        test_index = 158
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta159(self):
        test_index = 159
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta160(self):
        test_index = 160
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta161(self):
        test_index = 161
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta162(self):
        test_index = 162
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta163(self):
        test_index = 163
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta164(self):
        test_index = 164
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta165(self):
        test_index = 165
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta166(self):
        test_index = 166
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta167(self):
        test_index = 167
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta168(self):
        test_index = 168
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta169(self):
        test_index = 169
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta170(self):
        test_index = 170
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta171(self):
        test_index = 171
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta172(self):
        test_index = 172
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta173(self):
        test_index = 173
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta174(self):
        test_index = 174
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta175(self):
        test_index = 175
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta176(self):
        test_index = 176
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta177(self):
        test_index = 177
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta178(self):
        test_index = 178
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta179(self):
        test_index = 179
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta180(self):
        test_index = 180
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta181(self):
        test_index = 181
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta182(self):
        test_index = 182
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta183(self):
        test_index = 183
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta184(self):
        test_index = 184
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta185(self):
        test_index = 185
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta186(self):
        test_index = 186
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta187(self):
        test_index = 187
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta188(self):
        test_index = 188
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta189(self):
        test_index = 189
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta190(self):
        test_index = 190
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta191(self):
        test_index = 191
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta192(self):
        test_index = 192
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta193(self):
        test_index = 193
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta194(self):
        test_index = 194
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta195(self):
        test_index = 195
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta196(self):
        test_index = 196
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta197(self):
        test_index = 197
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta198(self):
        test_index = 198
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta199(self):
        test_index = 199
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta200(self):
        test_index = 200
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta201(self):
        test_index = 201
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta202(self):
        test_index = 202
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta203(self):
        test_index = 203
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta204(self):
        test_index = 204
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta205(self):
        test_index = 205
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta206(self):
        test_index = 206
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta207(self):
        test_index = 207
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta208(self):
        test_index = 208
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    def test_cuarta_pauta209(self):
        test_index = 209
        text = self.get_line(test_index)
            
        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
    
    
    def test_cuarta_pauta210(self):
        test_index = 210
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta211(self):
        test_index = 211
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta212(self):
        test_index = 212
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta213(self):
        test_index = 213
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta214(self):
        test_index = 214
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta215(self):
        test_index = 215
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta216(self):
        test_index = 216
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta217(self):
        test_index = 217
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta218(self):
        test_index = 218
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta219(self):
        test_index = 219
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta220(self):
        test_index = 220
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta221(self):
        test_index = 221
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta222(self):
        test_index = 222
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta223(self):
        test_index = 223
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta224(self):
        test_index = 224
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta225(self):
        test_index = 225
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta226(self):
        test_index = 226
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta227(self):
        test_index = 227
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta228(self):
        test_index = 228
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta229(self):
        test_index = 229
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta230(self):
        test_index = 230
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta231(self):
        test_index = 231
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta232(self):
        test_index = 232
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta233(self):
        test_index = 233
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta234(self):
        test_index = 234
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta235(self):
        test_index = 235
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta236(self):
        test_index = 236
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta237(self):
        test_index = 237
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta238(self):
        test_index = 238
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta239(self):
        test_index = 239
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta240(self):
        test_index = 240
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta241(self):
        test_index = 241
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta242(self):
        test_index = 242
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta243(self):
        test_index = 243
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta244(self):
        test_index = 244
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta245(self):
        test_index = 245
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta246(self):
        test_index = 246
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta247(self):
        test_index = 247
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta248(self):
        test_index = 248
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta249(self):
        test_index = 249
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta250(self):
        test_index = 250
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta251(self):
        test_index = 251
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta252(self):
        test_index = 252
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta253(self):
        test_index = 253
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta254(self):
        test_index = 254
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta255(self):
        test_index = 255
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta256(self):
        test_index = 256
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta257(self):
        test_index = 257
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta258(self):
        test_index = 258
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta259(self):
        test_index = 259
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta260(self):
        test_index = 260
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta261(self):
        test_index = 261
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta262(self):
        test_index = 262
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta263(self):
        test_index = 263
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta264(self):
        test_index = 264
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta265(self):
        test_index = 265
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta266(self):
        test_index = 266
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta267(self):
        test_index = 267
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta268(self):
        test_index = 268
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta269(self):
        test_index = 269
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta270(self):
        test_index = 270
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta271(self):
        test_index = 271
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta272(self):
        test_index = 272
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta273(self):
        test_index = 273
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta274(self):
        test_index = 274
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta275(self):
        test_index = 275
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta276(self):
        test_index = 276
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta277(self):
        test_index = 277
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta278(self):
        test_index = 278
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta279(self):
        test_index = 279
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta280(self):
        test_index = 280
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta281(self):
        test_index = 281
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta282(self):
        test_index = 282
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta283(self):
        test_index = 283
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta284(self):
        test_index = 284
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta285(self):
        test_index = 285
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta286(self):
        test_index = 286
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta287(self):
        test_index = 287
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta288(self):
        test_index = 288
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta289(self):
        test_index = 289
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta290(self):
        test_index = 290
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta291(self):
        test_index = 291
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta292(self):
        test_index = 292
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta293(self):
        test_index = 293
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta294(self):
        test_index = 294
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta295(self):
        test_index = 295
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta296(self):
        test_index = 296
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta297(self):
        test_index = 297
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta298(self):
        test_index = 298
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta299(self):
        test_index = 299
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta300(self):
        test_index = 300
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta301(self):
        test_index = 301
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta302(self):
        test_index = 302
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta303(self):
        test_index = 303
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta304(self):
        test_index = 304
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta305(self):
        test_index = 305
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta306(self):
        test_index = 306
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta307(self):
        test_index = 307
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta308(self):
        test_index = 308
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta309(self):
        test_index = 309
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta310(self):
        test_index = 310
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta311(self):
        test_index = 311
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta312(self):
        test_index = 312
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta313(self):
        test_index = 313
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta314(self):
        test_index = 314
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta315(self):
        test_index = 315
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta316(self):
        test_index = 316
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta317(self):
        test_index = 317
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta318(self):
        test_index = 318
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta319(self):
        test_index = 319
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta320(self):
        test_index = 320
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta321(self):
        test_index = 321
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta322(self):
        test_index = 322
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta323(self):
        test_index = 323
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta324(self):
        test_index = 324
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta325(self):
        test_index = 325
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta326(self):
        test_index = 326
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta327(self):
        test_index = 327
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta328(self):
        test_index = 328
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta329(self):
        test_index = 329
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta330(self):
        test_index = 330
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta331(self):
        test_index = 331
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta332(self):
        test_index = 332
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta333(self):
        test_index = 333
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta334(self):
        test_index = 334
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta335(self):
        test_index = 335
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta336(self):
        test_index = 336
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta337(self):
        test_index = 337
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta338(self):
        test_index = 338
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta339(self):
        test_index = 339
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta340(self):
        test_index = 340
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta341(self):
        test_index = 341
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta342(self):
        test_index = 342
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta343(self):
        test_index = 343
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta344(self):
        test_index = 344
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta345(self):
        test_index = 345
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta346(self):
        test_index = 346
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta347(self):
        test_index = 347
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta348(self):
        test_index = 348
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta349(self):
        test_index = 349
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta350(self):
        test_index = 350
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta351(self):
        test_index = 351
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta352(self):
        test_index = 352
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta353(self):
        test_index = 353
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta354(self):
        test_index = 354
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta355(self):
        test_index = 355
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta356(self):
        test_index = 356
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta357(self):
        test_index = 357
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta358(self):
        test_index = 358
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta359(self):
        test_index = 359
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta360(self):
        test_index = 360
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta361(self):
        test_index = 361
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta362(self):
        test_index = 362
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta363(self):
        test_index = 363
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta364(self):
        test_index = 364
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta365(self):
        test_index = 365
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta366(self):
        test_index = 366
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta367(self):
        test_index = 367
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta368(self):
        test_index = 368
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta369(self):
        test_index = 369
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta370(self):
        test_index = 370
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta371(self):
        test_index = 371
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta372(self):
        test_index = 372
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta373(self):
        test_index = 373
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta374(self):
        test_index = 374
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta375(self):
        test_index = 375
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta376(self):
        test_index = 376
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta377(self):
        test_index = 377
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta378(self):
        test_index = 378
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta379(self):
        test_index = 379
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta380(self):
        test_index = 380
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta381(self):
        test_index = 381
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta382(self):
        test_index = 382
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta383(self):
        test_index = 383
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta384(self):
        test_index = 384
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta385(self):
        test_index = 385
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta386(self):
        test_index = 386
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta387(self):
        test_index = 387
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta388(self):
        test_index = 388
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta389(self):
        test_index = 389
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta390(self):
        test_index = 390
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta391(self):
        test_index = 391
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta392(self):
        test_index = 392
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta393(self):
        test_index = 393
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta394(self):
        test_index = 394
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta395(self):
        test_index = 395
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta396(self):
        test_index = 396
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta397(self):
        test_index = 397
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta398(self):
        test_index = 398
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta399(self):
        test_index = 399
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta400(self):
        test_index = 400
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta401(self):
        test_index = 401
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta402(self):
        test_index = 402
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta403(self):
        test_index = 403
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta404(self):
        test_index = 404
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta405(self):
        test_index = 405
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta406(self):
        test_index = 406
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta407(self):
        test_index = 407
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta408(self):
        test_index = 408
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta409(self):
        test_index = 409
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta410(self):
        test_index = 410
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta411(self):
        test_index = 411
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta412(self):
        test_index = 412
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta413(self):
        test_index = 413
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta414(self):
        test_index = 414
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta415(self):
        test_index = 415
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta416(self):
        test_index = 416
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta417(self):
        test_index = 417
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta418(self):
        test_index = 418
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta419(self):
        test_index = 419
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta420(self):
        test_index = 420
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta421(self):
        test_index = 421
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta422(self):
        test_index = 422
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta423(self):
        test_index = 423
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta424(self):
        test_index = 424
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta425(self):
        test_index = 425
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta426(self):
        test_index = 426
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta427(self):
        test_index = 427
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta428(self):
        test_index = 428
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta429(self):
        test_index = 429
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta430(self):
        test_index = 430
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta431(self):
        test_index = 431
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta432(self):
        test_index = 432
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta433(self):
        test_index = 433
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta434(self):
        test_index = 434
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta435(self):
        test_index = 435
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta436(self):
        test_index = 436
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta437(self):
        test_index = 437
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta438(self):
        test_index = 438
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta439(self):
        test_index = 439
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta440(self):
        test_index = 440
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta441(self):
        test_index = 441
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta442(self):
        test_index = 442
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta443(self):
        test_index = 443
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
        
    def test_cuarta_pauta444(self):
        test_index = 444
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta445(self):
        test_index = 445
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta446(self):
        test_index = 446
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta447(self):
        test_index = 447
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta448(self):
        test_index = 448
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta449(self):
        test_index = 449
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta450(self):
        test_index = 450
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta451(self):
        test_index = 451
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta452(self):
        test_index = 452
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta453(self):
        test_index = 453
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta454(self):
        test_index = 454
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta455(self):
        test_index = 455
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta456(self):
        test_index = 456
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta457(self):
        test_index = 457
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta458(self):
        test_index = 458
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta459(self):
        test_index = 459
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta460(self):
        test_index = 460
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta461(self):
        test_index = 461
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta462(self):
        test_index = 462
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta463(self):
        test_index = 463
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta464(self):
        test_index = 464
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta465(self):
        test_index = 465
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta466(self):
        test_index = 466
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta467(self):
        test_index = 467
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta468(self):
        test_index = 468
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta469(self):
        test_index = 469
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta470(self):
        test_index = 470
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta471(self):
        test_index = 471
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta472(self):
        test_index = 472
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta473(self):
        test_index = 473
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta474(self):
        test_index = 474
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta475(self):
        test_index = 475
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta476(self):
        test_index = 476
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta477(self):
        test_index = 477
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta478(self):
        test_index = 478
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta479(self):
        test_index = 479
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta480(self):
        test_index = 480
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta481(self):
        test_index = 481
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta482(self):
        test_index = 482
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta483(self):
        test_index = 483
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta484(self):
        test_index = 484
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta485(self):
        test_index = 485
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta486(self):
        test_index = 486
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta487(self):
        test_index = 487
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta488(self):
        test_index = 488
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta489(self):
        test_index = 489
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta490(self):
        test_index = 490
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta491(self):
        test_index = 491
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta492(self):
        test_index = 492
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta493(self):
        test_index = 493
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta494(self):
        test_index = 494
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta495(self):
        test_index = 495
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta496(self):
        test_index = 496
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta497(self):
        test_index = 497
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta498(self):
        test_index = 498
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta499(self):
        test_index = 499
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta500(self):
        test_index = 500
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta501(self):
        test_index = 501
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta502(self):
        test_index = 502
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta503(self):
        test_index = 503
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta504(self):
        test_index = 504
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta505(self):
        test_index = 505
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta506(self):
        test_index = 506
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta507(self):
        test_index = 507
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta508(self):
        test_index = 508
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta509(self):
        test_index = 509
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta510(self):
        test_index = 510
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta511(self):
        test_index = 511
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta512(self):
        test_index = 512
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta513(self):
        test_index = 513
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta514(self):
        test_index = 514
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta515(self):
        test_index = 515
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta516(self):
        test_index = 516
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta517(self):
        test_index = 517
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta518(self):
        test_index = 518
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta519(self):
        test_index = 519
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta520(self):
        test_index = 520
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta521(self):
        test_index = 521
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta522(self):
        test_index = 522
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta523(self):
        test_index = 523
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta524(self):
        test_index = 524
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta525(self):
        test_index = 525
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta526(self):
        test_index = 526
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta527(self):
        test_index = 527
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta528(self):
        test_index = 528
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta529(self):
        test_index = 529
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta530(self):
        test_index = 530
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta531(self):
        test_index = 531
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta532(self):
        test_index = 532
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta533(self):
        test_index = 533
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta534(self):
        test_index = 534
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta535(self):
        test_index = 535
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta536(self):
        test_index = 536
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta537(self):
        test_index = 537
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta538(self):
        test_index = 538
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta539(self):
        test_index = 539
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta540(self):
        test_index = 540
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta541(self):
        test_index = 541
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta542(self):
        test_index = 542
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta543(self):
        test_index = 543
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta544(self):
        test_index = 544
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta545(self):
        test_index = 545
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta546(self):
        test_index = 546
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta547(self):
        test_index = 547
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta548(self):
        test_index = 548
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta549(self):
        test_index = 549
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta550(self):
        test_index = 550
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta551(self):
        test_index = 551
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta552(self):
        test_index = 552
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta553(self):
        test_index = 553
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta554(self):
        test_index = 554
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta555(self):
        test_index = 555
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta556(self):
        test_index = 556
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta557(self):
        test_index = 557
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta558(self):
        test_index = 558
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta559(self):
        test_index = 559
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta560(self):
        test_index = 560
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta561(self):
        test_index = 561
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta562(self):
        test_index = 562
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta563(self):
        test_index = 563
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta564(self):
        test_index = 564
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta565(self):
        test_index = 565
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta566(self):
        test_index = 566
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta567(self):
        test_index = 567
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta568(self):
        test_index = 568
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta569(self):
        test_index = 569
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta570(self):
        test_index = 570
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta571(self):
        test_index = 571
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta572(self):
        test_index = 572
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta573(self):
        test_index = 573
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta574(self):
        test_index = 574
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta575(self):
        test_index = 575
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta576(self):
        test_index = 576
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta577(self):
        test_index = 577
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta578(self):
        test_index = 578
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta579(self):
        test_index = 579
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta580(self):
        test_index = 580
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta581(self):
        test_index = 581
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta582(self):
        test_index = 582
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta583(self):
        test_index = 583
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta584(self):
        test_index = 584
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta585(self):
        test_index = 585
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta586(self):
        test_index = 586
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta587(self):
        test_index = 587
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta588(self):
        test_index = 588
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta589(self):
        test_index = 589
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta590(self):
        test_index = 590
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta591(self):
        test_index = 591
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta592(self):
        test_index = 592
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta593(self):
        test_index = 593
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta594(self):
        test_index = 594
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta595(self):
        test_index = 595
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta596(self):
        test_index = 596
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta597(self):
        test_index = 597
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta598(self):
        test_index = 598
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta599(self):
        test_index = 599
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta600(self):
        test_index = 600
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta601(self):
        test_index = 601
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta602(self):
        test_index = 602
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta603(self):
        test_index = 603
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta604(self):
        test_index = 604
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta605(self):
        test_index = 605
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta606(self):
        test_index = 606
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta607(self):
        test_index = 607
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta608(self):
        test_index = 608
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta609(self):
        test_index = 609
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta610(self):
        test_index = 610
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta611(self):
        test_index = 611
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta612(self):
        test_index = 612
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta613(self):
        test_index = 613
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta614(self):
        test_index = 614
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta615(self):
        test_index = 615
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta616(self):
        test_index = 616
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta617(self):
        test_index = 617
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta618(self):
        test_index = 618
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta619(self):
        test_index = 619
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta620(self):
        test_index = 620
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta621(self):
        test_index = 621
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta622(self):
        test_index = 622
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta623(self):
        test_index = 623
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta624(self):
        test_index = 624
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta625(self):
        test_index = 625
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta626(self):
        test_index = 626
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta627(self):
        test_index = 627
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta628(self):
        test_index = 628
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta629(self):
        test_index = 629
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta630(self):
        test_index = 630
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta631(self):
        test_index = 631
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta632(self):
        test_index = 632
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta633(self):
        test_index = 633
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta634(self):
        test_index = 634
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta635(self):
        test_index = 635
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta636(self):
        test_index = 636
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta637(self):
        test_index = 637
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta638(self):
        test_index = 638
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta639(self):
        test_index = 639
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta640(self):
        test_index = 640
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta641(self):
        test_index = 641
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta642(self):
        test_index = 642
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta643(self):
        test_index = 643
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta644(self):
        test_index = 644
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta645(self):
        test_index = 645
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta646(self):
        test_index = 646
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta647(self):
        test_index = 647
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta648(self):
        test_index = 648
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta649(self):
        test_index = 649
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta650(self):
        test_index = 650
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta651(self):
        test_index = 651
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta652(self):
        test_index = 652
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta653(self):
        test_index = 653
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta654(self):
        test_index = 654
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta655(self):
        test_index = 655
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta656(self):
        test_index = 656
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta657(self):
        test_index = 657
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta658(self):
        test_index = 658
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta659(self):
        test_index = 659
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta660(self):
        test_index = 660
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta661(self):
        test_index = 661
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta662(self):
        test_index = 662
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta663(self):
        test_index = 663
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta664(self):
        test_index = 664
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta665(self):
        test_index = 665
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta666(self):
        test_index = 666
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta667(self):
        test_index = 667
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta668(self):
        test_index = 668
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta669(self):
        test_index = 669
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta670(self):
        test_index = 670
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta671(self):
        test_index = 671
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta672(self):
        test_index = 672
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta673(self):
        test_index = 673
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta674(self):
        test_index = 674
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta675(self):
        test_index = 675
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta676(self):
        test_index = 676
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta677(self):
        test_index = 677
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta678(self):
        test_index = 678
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta679(self):
        test_index = 679
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta680(self):
        test_index = 680
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta681(self):
        test_index = 681
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta682(self):
        test_index = 682
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta683(self):
        test_index = 683
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta684(self):
        test_index = 684
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta685(self):
        test_index = 685
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta686(self):
        test_index = 686
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta687(self):
        test_index = 687
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta688(self):
        test_index = 688
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta689(self):
        test_index = 689
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta690(self):
        test_index = 690
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta691(self):
        test_index = 691
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta692(self):
        test_index = 692
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta693(self):
        test_index = 693
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta694(self):
        test_index = 694
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta695(self):
        test_index = 695
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta696(self):
        test_index = 696
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta697(self):
        test_index = 697
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta698(self):
        test_index = 698
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta699(self):
        test_index = 699
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta700(self):
        test_index = 700
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta701(self):
        test_index = 701
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta702(self):
        test_index = 702
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta703(self):
        test_index = 703
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta704(self):
        test_index = 704
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta705(self):
        test_index = 705
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta706(self):
        test_index = 706
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta707(self):
        test_index = 707
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta708(self):
        test_index = 708
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta709(self):
        test_index = 709
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta710(self):
        test_index = 710
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta711(self):
        test_index = 711
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta712(self):
        test_index = 712
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta713(self):
        test_index = 713
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta714(self):
        test_index = 714
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta715(self):
        test_index = 715
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta716(self):
        test_index = 716
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta717(self):
        test_index = 717
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta718(self):
        test_index = 718
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta719(self):
        test_index = 719
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta720(self):
        test_index = 720
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta721(self):
        test_index = 721
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta722(self):
        test_index = 722
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta723(self):
        test_index = 723
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta724(self):
        test_index = 724
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta725(self):
        test_index = 725
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta726(self):
        test_index = 726
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta727(self):
        test_index = 727
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta728(self):
        test_index = 728
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta729(self):
        test_index = 729
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta730(self):
        test_index = 730
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta731(self):
        test_index = 731
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta732(self):
        test_index = 732
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta733(self):
        test_index = 733
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta734(self):
        test_index = 734
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta735(self):
        test_index = 735
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta736(self):
        test_index = 736
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta737(self):
        test_index = 737
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta738(self):
        test_index = 738
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta739(self):
        test_index = 739
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta740(self):
        test_index = 740
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta741(self):
        test_index = 741
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta742(self):
        test_index = 742
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta743(self):
        test_index = 743
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta744(self):
        test_index = 744
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta745(self):
        test_index = 745
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta746(self):
        test_index = 746
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta747(self):
        test_index = 747
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta748(self):
        test_index = 748
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta749(self):
        test_index = 749
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta750(self):
        test_index = 750
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta751(self):
        test_index = 751
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta752(self):
        test_index = 752
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta753(self):
        test_index = 753
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta754(self):
        test_index = 754
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta755(self):
        test_index = 755
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta756(self):
        test_index = 756
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta757(self):
        test_index = 757
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta758(self):
        test_index = 758
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta759(self):
        test_index = 759
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta760(self):
        test_index = 760
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta761(self):
        test_index = 761
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta762(self):
        test_index = 762
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta763(self):
        test_index = 763
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta764(self):
        test_index = 764
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta765(self):
        test_index = 765
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta766(self):
        test_index = 766
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta767(self):
        test_index = 767
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta768(self):
        test_index = 768
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta769(self):
        test_index = 769
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta770(self):
        test_index = 770
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta771(self):
        test_index = 771
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta772(self):
        test_index = 772
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta773(self):
        test_index = 773
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta774(self):
        test_index = 774
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta775(self):
        test_index = 775
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta776(self):
        test_index = 776
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta777(self):
        test_index = 777
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta778(self):
        test_index = 778
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta779(self):
        test_index = 779
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta780(self):
        test_index = 780
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta781(self):
        test_index = 781
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta782(self):
        test_index = 782
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta783(self):
        test_index = 783
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta784(self):
        test_index = 784
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta785(self):
        test_index = 785
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta786(self):
        test_index = 786
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta787(self):
        test_index = 787
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta788(self):
        test_index = 788
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta789(self):
        test_index = 789
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta790(self):
        test_index = 790
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta791(self):
        test_index = 791
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta792(self):
        test_index = 792
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta793(self):
        test_index = 793
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta794(self):
        test_index = 794
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta795(self):
        test_index = 795
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta796(self):
        test_index = 796
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta797(self):
        test_index = 797
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta798(self):
        test_index = 798
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta799(self):
        test_index = 799
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta800(self):
        test_index = 800
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta801(self):
        test_index = 801
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta802(self):
        test_index = 802
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta803(self):
        test_index = 803
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta804(self):
        test_index = 804
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta805(self):
        test_index = 805
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta806(self):
        test_index = 806
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta807(self):
        test_index = 807
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta808(self):
        test_index = 808
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta809(self):
        test_index = 809
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta810(self):
        test_index = 810
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta811(self):
        test_index = 811
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta812(self):
        test_index = 812
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta813(self):
        test_index = 813
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta814(self):
        test_index = 814
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta815(self):
        test_index = 815
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta816(self):
        test_index = 816
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta817(self):
        test_index = 817
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta818(self):
        test_index = 818
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta819(self):
        test_index = 819
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta820(self):
        test_index = 820
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta821(self):
        test_index = 821
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta822(self):
        test_index = 822
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta823(self):
        test_index = 823
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta824(self):
        test_index = 824
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta825(self):
        test_index = 825
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta826(self):
        test_index = 826
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta827(self):
        test_index = 827
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta828(self):
        test_index = 828
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta829(self):
        test_index = 829
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta830(self):
        test_index = 830
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta831(self):
        test_index = 831
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta832(self):
        test_index = 832
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta833(self):
        test_index = 833
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta834(self):
        test_index = 834
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta835(self):
        test_index = 835
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta836(self):
        test_index = 836
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta837(self):
        test_index = 837
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta838(self):
        test_index = 838
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta839(self):
        test_index = 839
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta840(self):
        test_index = 840
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta841(self):
        test_index = 841
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta842(self):
        test_index = 842
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta843(self):
        test_index = 843
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta844(self):
        test_index = 844
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta845(self):
        test_index = 845
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta846(self):
        test_index = 846
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta847(self):
        test_index = 847
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta848(self):
        test_index = 848
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta849(self):
        test_index = 849
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta850(self):
        test_index = 850
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta851(self):
        test_index = 851
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta852(self):
        test_index = 852
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta853(self):
        test_index = 853
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta854(self):
        test_index = 854
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta855(self):
        test_index = 855
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta856(self):
        test_index = 856
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta857(self):
        test_index = 857
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta858(self):
        test_index = 858
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta859(self):
        test_index = 859
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta860(self):
        test_index = 860
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta861(self):
        test_index = 861
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta862(self):
        test_index = 862
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta863(self):
        test_index = 863
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta864(self):
        test_index = 864
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta865(self):
        test_index = 865
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta866(self):
        test_index = 866
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta867(self):
        test_index = 867
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta868(self):
        test_index = 868
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta869(self):
        test_index = 869
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta870(self):
        test_index = 870
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta871(self):
        test_index = 871
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta872(self):
        test_index = 872
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta873(self):
        test_index = 873
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta874(self):
        test_index = 874
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta875(self):
        test_index = 875
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
        
        self.assertEqual(str(passed), passed_txt)
        self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta876(self):
        test_index = 876
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta877(self):
        test_index = 877
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta878(self):
        test_index = 878
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta879(self):
        test_index = 879
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta880(self):
        test_index = 880
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta881(self):
        test_index = 881
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta882(self):
        test_index = 882
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta883(self):
        test_index = 883
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta884(self):
        test_index = 884
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta885(self):
        test_index = 885
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta886(self):
        test_index = 886
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta887(self):
        test_index = 887
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta888(self):
        test_index = 888
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta889(self):
        test_index = 889
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta890(self):
        test_index = 890
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta891(self):
        test_index = 891
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta892(self):
        test_index = 892
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta893(self):
        test_index = 893
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta894(self):
        test_index = 894
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta895(self):
        test_index = 895
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta896(self):
        test_index = 896
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta897(self):
        test_index = 897
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta898(self):
        test_index = 898
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta899(self):
        test_index = 899
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta900(self):
        test_index = 900
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta901(self):
        test_index = 901
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta902(self):
        test_index = 902
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta903(self):
        test_index = 903
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta904(self):
        test_index = 904
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta905(self):
        test_index = 905
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta906(self):
        test_index = 906
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta907(self):
        test_index = 907
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta908(self):
        test_index = 908
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta909(self):
        test_index = 909
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta910(self):
        test_index = 910
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta911(self):
        test_index = 911
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta912(self):
        test_index = 912
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta913(self):
        test_index = 913
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta914(self):
        test_index = 914
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta915(self):
        test_index = 915
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta916(self):
        test_index = 916
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta917(self):
        test_index = 917
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta918(self):
        test_index = 918
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta919(self):
        test_index = 919
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta920(self):
        test_index = 920
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            
    def test_cuarta_pauta921(self):
        test_index = 921
        text = self.get_line(test_index)

        if text:
            algoritmos      = Algorithms(text)
            passed, reason  = algoritmos.validador_cuarta_pauta()
            passed_txt, reason_txt = self.get_correct_line(test_index)
            
            self.assertEqual(str(passed), passed_txt)
            self.assertEqual(str(reason), reason_txt)
            