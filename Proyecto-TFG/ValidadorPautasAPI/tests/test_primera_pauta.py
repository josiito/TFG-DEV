from django.test import TestCase
from os import path, remove
from ..algorithms import Algorithms

class TestPrimeraPauta(TestCase):
    """ 
    Clase Test que comprueba la funcionalidad de la primera pauta:
        Se debería evitar el uso de palabras de contenido indeterminado
    """

    CONCORDANCIA = '-={Concordancia}=-'
    REFERENCIA   = '-={Referencia bibliográfica}=-'
    PATH         = path.dirname(path.abspath(__file__))

    MAX_LINES = 100

    def setUp(self):
        """ Se crea un fichero txt con los casos prueba formateados """
        remove(f'{self.PATH}/res/PalabrasContenidoIndet.txt') if path.exists(f'{self.PATH}/res/PalabrasContenidoIndet.txt') else None

        try:
            file_asunto   = open(f'{self.PATH}/data/ExportacionCORPESAsunto.txt', mode='r', encoding='UTF-8')
            file_cosa     = open(f'{self.PATH}/data/ExportacionCORPESCosa.txt'  , mode='r', encoding='UTF-8')
            file_to_write = open(f'{self.PATH}/res/palabrasContenidoIndet.txt'  , mode='a', newline='', encoding='UTF-8')

            # 100 casos con la palabra de contenido indeterminado "asunto"
            is_text, num_lines = False, 0
            for line in file_asunto:
                if (num_lines >= self.MAX_LINES): break
                if( self.CONCORDANCIA in line ):
                    is_text = True
                elif( self.REFERENCIA in line ):
                    is_text = False
                elif( is_text and line != '\n' ):
                    file_to_write.write(f'{num_lines}+--+{line}')
                    num_lines += 1

            # 100 casos con la palabra de contenido indeterminado "cosa"
            is_text, num_lines = False, 0
            for line in file_asunto:
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
            file_asunto.close()
            file_cosa.close()
            file_to_write.close()

    # def tearDown(self):
    #     """ Elimina un archivo csv despues de hacer todos los tests """
    #     remove(f'{self.PATH}/res/PalabrasContenidoIndet.txt) if path.exists(f'{self.PATH}/data/horas.csv') else None

    def get_line(self, test_index):
        text = ""
        try:
            textfile = open(f'{self.PATH}/res/PalabrasContenidoIndet.txt', mode='r', encoding='UTF-8')
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

    def test_primera_pauta0(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(0)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])

    def test_primera_pauta1(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(1)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])
    
    def test_primera_pauta2(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(2)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['un asunto'])
    
    def test_primera_pauta3(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(3)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])
    
    def test_primera_pauta4(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(4)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])

    def test_primera_pauta5(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(5)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta6(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(6)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])

    def test_primera_pauta7(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(7)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta8(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(8)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta9(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(9)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta10(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(10)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta11(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(11)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta12(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(12)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta13(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(13)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta14(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(14)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['asuntos'])

    def test_primera_pauta15(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(15)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['asuntos'])
    
    def test_primera_pauta16(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(16)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])

    def test_primera_pauta17(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(17)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta18(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(18)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['asunto'])
    
    def test_primera_pauta19(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(19)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['asuntos'])
    
    def test_primera_pauta20(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(20)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])
    
    def test_primera_pauta21(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(21)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])
    
    def test_primera_pauta22(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(22)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['asuntos'])
    
    def test_primera_pauta23(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(23)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta24(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(24)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])

    def test_primera_pauta25(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(25)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['asunto'])
    
    def test_primera_pauta26(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(26)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['este asunto'])

    def test_primera_pauta27(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(27)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta28(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(28)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])
    
    def test_primera_pauta29(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(29)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['cosas'])
    
    def test_primera_pauta30(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(30)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])
    
    def test_primera_pauta31(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(31)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['al asunto'])
    
    def test_primera_pauta32(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(32)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])
    
    def test_primera_pauta33(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(33)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta34(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(34)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])

    def test_primera_pauta35(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(35)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['unos asuntos'])
    
    def test_primera_pauta36(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(36)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])

    def test_primera_pauta37(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(37)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta38(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(38)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta39(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(39)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta40(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(40)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta41(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(41)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta42(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(42)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['del asunto'])
    
    def test_primera_pauta43(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(43)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])
    
    def test_primera_pauta44(self):
        """ Test de la primera pauta: Se debería evitar el uso de palabras de contenido indeterminado """
        text = self.get_line(44)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])

    def test_primera_pauta45(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(45)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['asuntos'])
    
    def test_primera_pauta46(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(46)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['asunto'])

    def test_primera_pauta47(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(47)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['asuntos'])
    
    def test_primera_pauta48(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(48)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta49(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(49)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta50(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(50)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, ['el asunto'])
    
    def test_primera_pauta51(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(51)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])
    
    def test_primera_pauta52(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(52)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['del asunto'])
    
    def test_primera_pauta53(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(53)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])
    
    def test_primera_pauta54(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(54)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])

    def test_primera_pauta55(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(55)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['al asunto'])
    
    def test_primera_pauta56(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(56)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])

    def test_primera_pauta57(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(57)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])
    
    def test_primera_pauta58(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(58)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['los asuntos'])
    
    def test_primera_pauta59(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(59)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta60(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(60)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta61(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(61)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['asunto'])
    
    def test_primera_pauta62(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(62)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['asuntos'])
    
    def test_primera_pauta63(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(63)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])
    
    def test_primera_pauta64(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(64)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['los asuntos'])

    def test_primera_pauta65(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(65)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta66(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(66)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])

    def test_primera_pauta67(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(67)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['del asunto'])
    
    def test_primera_pauta68(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(68)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['del asunto'])
    
    def test_primera_pauta69(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(69)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta70(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(70)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])

    def test_primera_pauta71(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(71)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta72(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(72)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['asuntos'])
    
    def test_primera_pauta73(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(73)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['cosas', 'el asunto'])
    
    def test_primera_pauta74(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(74)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, [])

    def test_primera_pauta75(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(75)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['del asunto'])
    
    def test_primera_pauta76(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(76)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])

    def test_primera_pauta77(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(77)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['un asunto'])
    
    def test_primera_pauta78(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(78)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, ['asuntos'])
    
    def test_primera_pauta79(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(79)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta80(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(80)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto'])

    def test_primera_pauta81(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(81)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta82(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(82)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta83(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(83)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['del asunto'])
    
    def test_primera_pauta84(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(84)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])

    def test_primera_pauta85(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(85)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta86(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(86)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])

    def test_primera_pauta87(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(87)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta88(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(88)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta89(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(89)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta90(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(90)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])

    def test_primera_pauta91(self):
        """ No debe fallar. Las palabras que se podrian considerar de contenido indeterminado se entienden por contexto """
        text = self.get_line(91)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertTrue(passed)
            self.assertListEqual(reason, [])
    
    def test_primera_pauta92(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(92)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['algo', 'el asunto'])
    
    def test_primera_pauta93(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(93)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['El asunto'])
    
    def test_primera_pauta94(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(94)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['al asunto'])

    def test_primera_pauta95(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(95)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['este asunto'])
    
    def test_primera_pauta96(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(96)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['Asunto', 'el asunto'])

    def test_primera_pauta97(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(97)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['Asunto', 'el asunto'])
    
    def test_primera_pauta98(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(98)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['el asunto', 'algo'])
    
    def test_primera_pauta99(self):
        """ Debe fallar. No es suficiente el contexto """
        text = self.get_line(99)
        if text:
            algoritmos = Algorithms(text)
            passed, reason = algoritmos.validador_primera_pauta()

            self.assertFalse(passed)
            self.assertListEqual(reason, ['ciertos asuntos'])