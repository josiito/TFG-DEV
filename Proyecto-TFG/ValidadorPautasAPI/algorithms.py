from pickle import NONE
from spacy.matcher import Matcher

import spacy

class Algorithms():
    """ Clase que recogera los algoritmos de PLN para comprobar el cumplimiento de las cuatro pautas que se han desarrollado. """

    HORAS = {
        'madrugada': list([ hora for hora in range(1, 6)   ]),
        'mañana'   : list([ hora for hora in range(6, 13)  ]),
        'tarde'    : list([ hora for hora in range(12, 19) ]),
        'noche'    : list([ hora for hora in range(18, 25) ]),
    }

    PATRONES_PRIMERA_PAUTA = [
        [ { "POS": "DET", "DEP": "det" } , { "POS": "NOUN", "DEP": { "IN": [ "nsubj", "obj" ] } } ],
        [ { "MORPH": { "IS_SUPERSET": [ "PronType=Ind" ] } } ]
    ]

    PATRONES_CUARTA_PAUTA = [
        [ { "POS": "ADP"  }, { "POS": "NOUN" }                    ], # e.j. Sin embargo
        [ { "POS": "ADP"  }, { "POS": "PRON" }, { "POS": "NOUN" } ], # e.j. Por lo tanto
        [ { "POS": "PART" }, { "POS": "NOUN" }                    ], # e.j. No obstante
        [ 
            { "POS": { "IN": [ "ADV", "NOUN" ] }, "DEP": { "IN": [ "advmod", "mark" ] }  }, 
            { "POS": "SCONJ", "DEP": { "IN": [ "fixed", "mark" ] } },
        ],
    ]

    def __init__(self, texto: str = NONE):
        # Si el contenido del texto es vacio o no esta instanciado, se lanza un error
        if texto == NONE or not texto:
            raise TypeError('No se ha encontrado ningún contenido de texto.')

        self.nlp = spacy.load("es_core_news_sm")
        self.doc = self.nlp(texto)
        
        # Intancia del matcher
        self.matcher = Matcher(self.nlp.vocab)

    def validador_primera_pauta(self):
        """ Primera pauta: Se debería evitar el uso de palabras de contenido indeterminado """

        self.matcher.add('PATRONES_PRIMERA_PAUTA', self.PATRONES_PRIMERA_PAUTA)
        matches = self.matcher(self.doc)

        # Se crean la lista por la que posiblemente no cumpla la pauta
        reason = [ self.doc[start:end].text for _, start, end in matches ]

        # Se elimina el patron de la cuarta pauta para evitar colisiones no deseadas
        self.matcher.remove('PATRONES_PRIMERA_PAUTA')
        
        return len(reason) == 0, list(reason)

    def validador_segunda_pauta(self):
        """ Segunda pauta: Los numeros de telefono se deberian separar por bloques """
        
        reason = []

        # Bucle para recorrer los tokens del documento analizado por spaCy
        for token in self.doc:
            # Obtenemos el token que es un número
            if token.like_num:
                num = token.text
                # Comprobamos que sea un número de teléfono válido y sin separación de bloques
                if len(num) == 9:
                    reason.append('El número de telefono {} debería escribirse por bloques'.format(num))

        # Si no cumple con la pauta, se devuelve una posible corección
        # correccion = self.doc.text.replace(num, sol_prop)
        
        return len(reason) == 0, reason #, correccion

    def validador_tercera_pauta(self):
        """ Tercera pauta: Evitar escribir la hora en formato 24h """

        reason: list = []

        for token in self.doc:
            
            # Si el token es un token numérico o un token objeto, se analiza
            if token.pos_ in ['NUM', 'NOUN']:
                hora = token.text.split(':')

                # Se comprueba el formato hh:mm. Si lo cumple, no puede satisfacer la pauta
                if len(hora) == 2 and int(hora[0]) - 12 > 0:
                    reason.append('El numero {} esta escrito en formato 24h'.format(token.text))

        return len(reason) == 0, reason # , correccion

    def validador_cuarta_pauta(self):
        """ Cuarta pauta: Evitar el uso de conectores complejos entre oraciones """

        # Se crea el matcher con el patron correspondiente y se analiza el documento
        self.matcher.add('PATRONES_CUARTA_PAUTA', self.PATRONES_CUARTA_PAUTA)
        matches = self.matcher(self.doc)

        reason = [ self.doc[start:end].text for _, start, end in matches ]        
        
        # Se elimina el patron de la cuarta pauta para evitar colisiones indeseadas
        self.matcher.remove('PATRONES_CUARTA_PAUTA')

        # self.print_all_tokens()
        
        return len(matches) == 0, reason
            
    def print_all_tokens(self):
        for token in self.doc:
            print('+ ------------------------------------------- +')
            print('Token: {} - pos: {} - dep: {} - morph: {}'.format(token.text, token.pos_, token.dep_, token.morph))
            print('pos definition: {}'.format(spacy.explain(token.pos_)))
            print('definicion de dependencia: {}'.format(spacy.explain(token.dep_)))
            print('+ ------------------------------------------- +\n')
