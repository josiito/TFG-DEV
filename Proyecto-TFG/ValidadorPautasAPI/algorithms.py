import spacy

class Algorithms():
    """
    Clase que recogera los algoritmos de PLN para comprobar el cumplimiento de las cuatro pautas que se han desarrollado.
    """

    HORAS = {
        'madrugada': list([ hora for hora in range(1, 6)   ]),
        'mañana'   : list([ hora for hora in range(6, 13)  ]),
        'tarde'    : list([ hora for hora in range(12, 19) ]),
        'noche'    : list([ hora for hora in range(18, 25) ]),
    }

    def __init__(self, texto: str):
        if not texto:
            raise Exception('Es necesario pasar un texto para analizar')

        self.nlp = spacy.load("es_core_news_sm")
        self.doc = self.nlp(texto)

    def validador_primera_pauta(self):
        """ Primera pauta: Se debería evitar el uso de palabras de contenido indeterminado """
        pass

    def validador_segunda_pauta(self):
        """ Segunda pauta: Los numeros de telefono se deberian separar por bloques """
        
        reason: list    = []
        passed: bool    = True
        correccion: str = ''

        for token in self.doc:

            if token.like_num:
                num: str = token.text
                sol_prop: str = f'{num[0:3]} {num[3:5]} {num[5:7]} {num[7:9]}'

                if len(num) == 9:
                    passed = False
                    reason.append('El número de telefono {} debería escribirse por bloques'.format(num))

        if not passed:
            correccion = self.doc.text.replace(num, sol_prop)
        
        return passed, reason, correccion

    def validador_tercera_pauta(self):
        """ Tercera pauta: Se debera escribir la hora en formato 24h """

        passed: bool    = True
        reason: list    = []
        # problems: list  = []
        # correccion: str   = ''
        for token in self.doc:
            if token.pos_ in ['NUM', 'NOUN']:
                hora = token.text.split(':')
                if len(hora) == 2:
                    passed = False
                    reason.append('El numero {} no esta escrito en formato 24h'.format(token.text))
                    # problems.append('{}'.format(token.text))
        
        # if not passed:
        #     correccion = self._corrector_tercera_pauta(problems)
        
        return passed, reason # , correccion

    def validador_cuarta_pauta(self):
        """ Cuarta pauta: Evitar el uso de conectores complejos entre oraciones """
        pass

    def analisis_completo(self):
        """ Se analizara el contenido del documento completo que se pasara como parametro """
        pass

    # def _corrector_tercera_pauta(self, problems: list) -> str:
    #     """
    #     Corrector de la tercer pauta
    #     """

    #     texto = self.doc.text
    #     for problem in problems:
    #         splitter = problem.split(':')
    #         hora, minuto = splitter

    #         if minuto == '0' or minuto == '00':
    #             dia = ''
                
    #             i = 0
    #             for horas in list(self.HORAS.values()):
    #                 print(f'Son las: {hora}')
    #                 print(horas)
    #                 print(f'{hora in horas}')
    #                 print('+ ---------------------------------- +')
    #                 if hora in horas:
    #                     print('Son las', hora)
    #                     dia = self.HORAS.keys()
    #                 else:
    #                     i += 1

    #             texto = texto.replace(problem, f'{int(hora) - 12 if int(hora) > 12 else hora} de la {dia}')
    #         else:
    #             texto = texto.replace(problem, '-- en construccion --')
        
    #     return texto