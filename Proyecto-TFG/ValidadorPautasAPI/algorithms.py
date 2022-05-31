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

    def __init__(self, texto: str = None):
        # Si el contenido del texto es vacio o no esta instanciado, se lanza un error
        if texto == None or not texto:
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
        
        reasons = []

        # Obtengo las oraciones que tengan la palabra 'teléfono', 'número' o 'móvil. Si las tienen las analizo mas adelante.
        sentences_map    = map(
            lambda sentence: sentence if sentence.text.lower().find('teléfono') != -1 or 
                                        sentence.text.lower().find('número')    != -1 or 
                                        sentence.text.lower().find('móvil')     != -1 else None, 
            self.doc.sents
        )
        # Elimino los None de la lista de oraciones (por la condicion else).
        sentences_filter = list(filter(lambda sentence: sentence != None, sentences_map))

        # Si solo se ha encontrado una oracion con la palabra 'teléfono', 'número' o 'móvil', se analiza sola
        if  0 < len(sentences_filter) <= 1:
            for token in sentences_filter[0]:
                if token.like_num and len(token.text) == 9:
                    if token.text not in reasons:
                        reasons.append(token.text)

        # Se se han encontrado mas, se encuentran correlaciones entre las oraciones i e i+1 y se analizan ambas si su ratio de relacion es mayor o igual que 0.4
        # Este indice se ha obtenido a partir de pruebas.
        else:
            i = 0
            while i+1 < len(sentences_filter):
                similarity = sentences_filter[i].similarity(sentences_filter[i+1])
                if round(similarity, 2) >= 0.40:
                    docs = [sentences_filter[i], sentences_filter[i+1]]
                    for doc in docs:
                        for token in doc:
                            if token.like_num and len(token.text) == 9:
                                if token.text not in reasons:
                                    reasons.append(token.text)
                i += 1

        # Si no cumple con la pauta, se devuelve una posible corección
        correccion = []
        if len(reasons) > 0:
            for reason in reasons:
                correccion.append(f'{reason[0:2]}-{reason[2:5]}-{reason[5:7]}-{reason[7:9]}')
        
        return len(reasons) == 0, reasons, correccion

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
