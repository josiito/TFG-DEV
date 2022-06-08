from spacy.matcher import Matcher
import spacy

class Algorithms():
    """ Clase que recogera los algoritmos de PLN para comprobar el cumplimiento de las cuatro pautas que se han desarrollado. """

    PATRONES_PRIMERA_PAUTA = [
        [ { "POS": "DET", "DEP": "det" } , { "POS": "NOUN", "DEP": { "IN": [ "nsubj", "obj" ] } } ],
        [ { "MORPH": { "IS_SUPERSET": [ "PronType=Ind" ] } } ]
    ]

    # ------------------------------------------------ #
    # Patrones de la tercera pauta
    PATRON_HORA_SIMPLE = [
        [ 
            { 'POS': { 'IN': [ 'NOUN', 'NUM' ] }, 'MORPH': { 'IS_SUBSET': [ 'NumForm=Digit', 'NumType=Card', 'AdvType=Tim' ] } } 
        ], # ej: a las 20:45
    ]
    # Patron que identifica frases como: 10 minutos despues/antes de las 12 [ y media/cuarto/diez de la  ]
    PATRON_HORA_COMPLEX = [
        [
            { 'POS': 'NUM'  }, # ej: cualquier numero (serian los minutos)
            { 'LEMMA': 'minuto',  'OP': '?' }, # ej: minutos
            { 'POS': 'ADV', 'DEP': 'advmod' }, # ej: despues o antes
            { 'ORTH': 'de'  },
            { 'ORTH': 'las' },
            { 'POS': 'NUM'  }, # ej: cualquier numero (serian las horas)
        ],
        [
            { 'POS': 'NUM'  }, # ej: cualquier numero (serian los minutos)
            { 'LEMMA': 'minuto',  'OP': '?' }, # ej: minutos
            { 'POS': 'ADV', 'DEP': 'advmod' }, # ej: despues o antes
            { 'ORTH': 'de'  },
            { 'ORTH': 'las' },
            { 'POS': 'NUM'  }, # ej: cualquier numero (serian las horas)
            { 'ORTH': 'y', 'OP': '?'    }, # puede aparecer o no
            { 'POS': 'NUM', 'OP': '?'   }, # ej: (y) media, cuarto o diez 
            { 'LEMMA': 'de', 'OP': '?'  },
            { 'ORTH': 'la', 'OP': '?'   },
            { 'POS': 'NOUN', 'DEP': 'nmod', 'OP': '?' }, # ej: mañana, tarde o
        ]
    ]
    # ------------------------------------------------ #

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
            self.doc.sents)

        # Elimino los None de la lista de oraciones (por la condicion else).
        sentences_filter = list(filter(lambda sentence: sentence != None, sentences_map))

        # Si solo se ha encontrado una oracion con la palabra 'teléfono', 'número' o 'móvil', se analiza sola
        if  0 < len(sentences_filter) <= 1:
            for token in sentences_filter[0]:
                if token.like_num and len(token.text) == 9:
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
                                reasons.append(token.text)
                i += 1

        # Si no cumple con la pauta, se devuelve una posible corección
        correccion = []
        if len(reasons) > 0:
            for reason in reasons:
                correccion.append(f'{reason[0:3]}-{reason[3:5]}-{reason[5:7]}-{reason[7:9]}')

        return len(reasons) == 0, reasons, correccion

    def validador_tercera_pauta(self):
        """ Tercera pauta: Evitar escribir la hora en formato 24h """

        self.matcher.add('PATRON_SIMPLE', self.PATRON_HORA_SIMPLE)
        self.matcher.add('PATRON_COMPLEX', self.PATRON_HORA_COMPLEX, on_match=self.eliminar_elementos_repetidos)
        
        matches = self.matcher(self.doc)
        tokens  = [ self.doc[start:end] for _, start, end in matches ]
        
        mapping = dict()
        for match_id, start, end in matches:
            mapping[match_id] = self.doc[start:end].text

        result, correccion = [], []
        for _, case in enumerate(tokens):
            if len( formato := case.text.split(':') ) == 2:
                # En este caso la hora esta escrito en formato 12h y no 24h
                if ( int(formato[0]) - 12 ) <= 0:
                    pass
                else:
                    result.append(case.text)
                    correccion.append(f'{int(formato[0]) - 12}:{formato[1]}')
            else:
                tokens_in_span = [ token for token in case ]
                if len(tokens_in_span) > 1:
                    result.append(case.text)

        self.matcher.remove('PATRON_SIMPLE')
        self.matcher.remove('PATRON_COMPLEX')

        return len(result) == 0, result, correccion

    def validador_cuarta_pauta(self):
        """ Cuarta pauta: Evitar el uso de conectores complejos entre oraciones """

        # Se crea el matcher con el patron correspondiente y se analiza el documento
        self.matcher.add('PATRONES_CUARTA_PAUTA', self.PATRONES_CUARTA_PAUTA)
        matches = self.matcher(self.doc)

        reason = [ self.doc[start:end].text for _, start, end in matches ]        
        
        # Se elimina el patron de la cuarta pauta para evitar colisiones indeseadas
        self.matcher.remove('PATRONES_CUARTA_PAUTA')
        
        return len(reason) == 0, reason
    
    # Recibe como parametros: matcher, doc, i, matches
    def eliminar_elementos_repetidos(self, matcher, doc, i, matches):
        """ En cada match elimina de la lista matches el caso anterior si los identificadores son iguales (repetidos) """
        match_id, _, _ = matches[i]
        if i >= 1:
            match_id_last, _, _ = matches[i-1]
            if match_id == match_id_last:
                del matches[i-i]
    
    def eliminar_repetidos(self, lista_a ,lista_b) -> list:
        lista_res = []
        for item in lista_a:
            for item_rep in lista_b:
                if item in item_rep:
                    continue
                else:
                    lista_res.append(item)
        return lista_res
