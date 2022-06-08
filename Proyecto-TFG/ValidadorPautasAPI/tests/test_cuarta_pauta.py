from django.test import TestCase
from os import path, remove
from ..algorithms import Algorithms

class TestCuartaPauta(TestCase):
    """ 
    Clase Test que comprueba la funcionalidad de la segunda pauta:
        Evitar el uso de conectores complejos entre oraciones
    """

    PATH = path.dirname(path.abspath(__file__))

    def setUp(self):
        """ Se crea un fichero txt con los casos prueba formateados """
        remove(f'{self.PATH}/res/conectores_complejos.txt') if path.exists(f'{self.PATH}/res/conectores_complejos.txt') else None

        with open(f'{self.PATH}/data/ExportacionEjemplosConectoresComplejos.txt', mode='r', encoding='UTF-8') as file_asunto:
            with open(f'{self.PATH}/res/conectores_complejos.txt', mode='w', newline='', encoding='UTF-8') as textfile:
                i = 0
                for line in file_asunto:
                    textfile.write(f'{i}+--+{line}')
                    i += 1

    def get_line(self, test_index):
        text = ""
        try:
            textfile = open(f'{self.PATH}/res/conectores_complejos.txt', mode='r', encoding='UTF-8')
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

    def test_cuarta_pauta0(self):
        text = self.get_line(0)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()

            # No debe fallar
            self.assertFalse( passed )
            self.assertEqual(reason[0], "así que")

    def test_cuarta_pauta1(self):
        text = self.get_line(1)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()

            self.assertFalse( passed )
            self.assertEqual(reason[0], "así que")
    
    def test_cuarta_pauta2(self):
        text = self.get_line(2)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            
            self.assertFalse( passed )
            self.assertEqual(reason[0], "así que")
    
    def test_cuarta_pauta3(self):
        text = self.get_line(3)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()

            self.assertTrue( passed )
    
    def test_cuarta_pauta4(self):
        text = self.get_line(4)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse(passed)
            self.assertEqual(reason[0], "Por ende")

    def test_cuarta_pauta5(self):
        text = self.get_line(5)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "por ende")
    
    def test_cuarta_pauta6(self):
        text = self.get_line(6)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "por tanto")

    def test_cuarta_pauta7(self):
        text = self.get_line(7)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "De cualquier modo")
    
    def test_cuarta_pauta8(self):
        text = self.get_line(8)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertTrue( passed )
    
    def test_cuarta_pauta9(self):
        text = self.get_line(9)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertTrue( passed )
    
    def test_cuarta_pauta10(self):
        text = self.get_line(10)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertTrue( passed )
    
    def test_cuarta_pauta11(self):
        text = self.get_line(11)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertTrue( passed )
    
    def test_cuarta_pauta12(self):
        text = self.get_line(12)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertTrue( passed )
    
    def test_cuarta_pauta13(self):
        text = self.get_line(13)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "sin embargo")

    def test_cuarta_pauta14(self):
        text = self.get_line(14)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "sin embargo")
    
    def test_cuarta_pauta15(self):
        text = self.get_line(0)        
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertTrue( passed )
    
    def test_cuarta_pauta16(self):
        text = self.get_line(16)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertTrue( passed )
    
    def test_cuarta_pauta17(self):
        text = self.get_line(17)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "así que")
    
    def test_cuarta_pauta18(self):
        text = self.get_line(18)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "así que")
    
    def test_cuarta_pauta19(self):
        text = self.get_line(19)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "de ahí que")
    
    def test_cuarta_pauta20(self):
        text = self.get_line(20)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "ahí que")
    
    def test_cuarta_pauta21(self):
        text = self.get_line(21)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "de ahí que")
    
    def test_cuarta_pauta22(self):
        text = self.get_line(22)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "por lo que")

    def test_cuarta_pauta23(self):
        text = self.get_line(23)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "por lo que")
    
    def test_cuarta_pauta24(self):
        text = self.get_line(24)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "de modo que")
    
    def test_cuarta_pauta25(self):
        text = self.get_line(25)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "de modo")

    def test_cuarta_pauta26(self):
        text = self.get_line(26)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "de modo")

    def test_cuarta_pauta27(self):
        text = self.get_line(27)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "de modo")
    
    def test_cuarta_pauta28(self):
        text = self.get_line(28)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertTrue( passed )
    
    def test_cuarta_pauta29(self):
        text = self.get_line(29)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertTrue( passed )
    
    def test_cuarta_pauta30(self):
        text = self.get_line(30)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "por lo tanto")
    
    def test_cuarta_pauta31(self):
        text = self.get_line(31)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "por lo tanto")
    
    def test_cuarta_pauta32(self):
        text = self.get_line(32)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "por lo tanto")

    def test_cuarta_pauta33(self):
        text = self.get_line(33)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "en consecuencia")
    
    def test_cuarta_pauta34(self):
        text = self.get_line(34)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertTrue( passed )
    
    def test_cuarta_pauta35(self):
        text = self.get_line(35)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertFalse( passed )
            self.assertEqual(reason[0], "por tanto")

    def test_cuarta_pauta36(self):
        text = self.get_line(36)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertTrue( passed )
    
    def test_cuarta_pauta37(self):
        text = self.get_line(37)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertTrue( passed )
    
    def test_cuarta_pauta38(self):
        text = self.get_line(38)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertTrue( passed )
    
    def test_cuarta_pauta39(self):
        text = self.get_line(39)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_cuarta_pauta()
            self.assertTrue( passed )