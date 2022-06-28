from spacy.matcher import Matcher
import spacy

class Algorithms():
    """ Clase que recogera los algoritmos de PLN para comprobar el cumplimiento de las cuatro pautas que se han desarrollado. """

    PATRONES_PRIMERA_PAUTA = [
        [ { "MORPH": { "IS_SUPERSET": [ "PronType=Ind" ] } } ]
    ]

    # ------------------------------------------------ #
    PATRON_HORA_SIMPLE = [
        [ 
            { 'POS': { 'IN': [ 'NOUN', 'NUM' ] }, 'MORPH': { 'IS_SUBSET': [ 'NumForm=Digit', 'NumType=Card', 'AdvType=Tim' ] } } 
        ], # ej: a las 20:45
    ]
    PATRON_HORA_COMPLEX = [
        [ 
            { 'POS': 'ADV' }, { 'LOWER': 'de' }, { 'LOWER': 'las' }, { 'POS': 'NUM' }, 
            { 'LOWER': 'de' }, { 'LOWER': 'la' }, { 'DEP': 'nmod' }
        ], # ej: después de las seis/6 de la tarde
        [ 
            { 'POS': 'NUM' }, { 'LEMMA': 'minuto' }, { 'POS': 'ADV' }, 
            { 'LOWER': 'de' }, { 'LOWER': 'las' }, { 'POS': 'NUM' } 
        ], # ej: 10 minutos despues/antes de las 11
    ]
    # ------------------------------------------------ #
    # Patrones cuarta pauta
    CONECTORES_ADVERSATIVOS_PATRON = [
        [ { 'LOWER': 'ahora' }, {'LOWER': 'bien'} ], 
        [ { 'LOWER': 'al'}, { 'LOWER': 'contrario' } ], 
        [ { 'LOWER': 'así' }, {'LOWER': 'y'},  {'LOWER': 'todo' } ], 
        [ { 'LOWER': 'con' }, { 'LOWER': 'todo' } ], 
        [ { 'LOWER': 'eso' }, {'LOWER': 'sí' } ],
        [ { 'LOWER': 'en' }, { 'LOWER': 'cambio' } ], 
        [ { 'LOWER': 'no'}, { 'LOWER': 'obstante' } ], 
        [ { 'LOWER': 'por'}, { 'LOWER': 'el' }, { 'LOWER': 'contrario' } ], 
        [ { 'LOWER': 'sin'}, { 'LOWER': 'embargo' } ],
        [ { 'LOWER': 'todo'}, { 'LOWER': 'lo' }, { 'LOWER': 'contrario' } ],
    ]
    CONECTORES_CONSECUTIVOS_PATRON = [
        [ { 'LOWER': 'así' }, {'LOWER': 'pues'} ], 
        [ { 'LOWER': 'de'}, { 'LOWER': 'este' }, { 'LOWER': 'modo' } ],
        [ { 'LOWER': 'de'}, { 'LOWER': 'ese' }, { 'LOWER': 'modo' } ],
        [ { 'LOWER': 'en' }, {'LOWER': 'consecuencia'} ],
        [ { 'LOWER': 'por' }, {'LOWER': 'consiguiente'} ],
        [ { 'LOWER': 'por' }, {'LOWER': 'ende'} ],
        [ { 'LOWER': 'por'}, { 'LOWER': 'esta' }, { 'LOWER': 'razón' } ],
        [ { 'LOWER': 'por' }, {'LOWER': 'tanto'} ],
        [ { 'LOWER': 'por'}, { 'LOWER': 'lo' }, { 'LOWER': 'tanto' } ],
    ]
    CONECTORES_RECAPILUTIVOS_PATRON = [
        [ { 'LOWER': 'a' }, {'LOWER': 'fin'}, {'LOWER': 'de'}, {'LOWER': 'cuentas'} ],
        [ { 'LOWER': 'al' }, {'LOWER': 'fin'}, {'LOWER': 'y'}, {'LOWER': 'al'}, {'LOWER': 'cabo'} ],
        [ { 'LOWER': 'en' }, {'LOWER': 'conclusión'} ],
        [ { 'LOWER': 'en' }, {'LOWER': 'suma'} ],
        [ { 'LOWER': 'en'}, { 'LOWER': 'una' }, { 'LOWER': 'palabra' } ],
    ]
    CONECTORES_ORDENACION_PATRON = [
        [ { 'LOWER': 'antes' }, {'LOWER': 'de'}, {'LOWER': 'nada'} ],
        [ { 'LOWER': 'en' }, {'LOWER': 'primer'}, {'LOWER': 'lugar'} ],
        [ { 'LOWER': 'para' }, {'LOWER': 'empezar'} ],

        [ { 'LOWER': 'a' }, {'LOWER': 'continuación'} ],
        [ { 'LOWER': 'en' }, {'LOWER': 'este'}, {'LOWER': 'momento'} ],
        [ { 'LOWER': 'en' }, {'LOWER': 'ese'}, {'LOWER': 'momento'} ],
        [ { 'LOWER': 'en' }, {'LOWER': 'ese'}, {'LOWER': 'preciso'}, {'LOWER': 'instante'} ],
        [ { 'LOWER': 'mientras' }, {'LOWER': 'tanto'} ],
        [ { 'LOWER': 'de' }, {'LOWER': 'pronto'} ],
        [ { 'LOWER': 'de' }, {'LOWER': 'repente'} ],

        [ { 'LOWER': 'en' }, {'LOWER': 'último'}, {'LOWER': 'lugar'} ],
        [ { 'LOWER': 'para' }, {'LOWER': 'terminar'} ],
    ]

    def __init__(self, texto: str = None):
        self.nlp = spacy.load('es_core_news_sm')
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
        sentences_filter = list(filter(lambda sentence: sentence != None and sentence.text != '\n' and sentence.text != '', sentences_map))

        # Si solo se ha encontrado una oracion con la palabra 'teléfono', 'número' o 'móvil', se analiza sola
        if  0 < len(sentences_filter) <= 1:
            for token in sentences_filter[0]:
                if token.like_num and len(token.text) == 9:
                    if '.' not in token.text and ',' not in token.text:
                        reasons.append(token.text)

        # Se se han encontrado mas, se encuentran correlaciones entre las oraciones i e i+1 y se analizan ambas si su ratio de relacion es mayor o igual que 0.4
        # Este indice se ha obtenido a partir de pruebas.
        else:
            i = 0
            while i+1 < len(sentences_filter):
                docs = [sentences_filter[i], sentences_filter[i+1]]
                for doc in docs:
                    for token in doc:
                        if token.like_num and len(token.text) == 9:
                            if '.' not in token.text and ',' not in token.text:
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
        self.matcher.add('PATRON_COMPLEX', self.PATRON_HORA_COMPLEX)
        
        matches = self.matcher(self.doc)
        tokens  = [ self.doc[start:end] for _, start, end in matches ]

        result, correccion = [], []
        for _, case in enumerate(tokens):
            if len( formato := case.text.split(':') ) == 2 and \
                '.' not in case.text:
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

        self.matcher.add('CONECTORES_ADVERSATIVOS_PATRON' , self.CONECTORES_ADVERSATIVOS_PATRON)
        self.matcher.add('CONECTORES_CONSECUTIVOS_PATRON' , self.CONECTORES_CONSECUTIVOS_PATRON)
        self.matcher.add('CONECTORES_RECAPILUTIVOS_PATRON', self.CONECTORES_RECAPILUTIVOS_PATRON)
        self.matcher.add('CONECTORES_ORDENACION_PATRON'   , self.CONECTORES_ORDENACION_PATRON)

        matches = self.matcher(self.doc)
        reason = [ self.doc[start:end].text for _, start, end in matches ]
        
        # Se elimina el patron de la cuarta pauta para evitar colisiones indeseadas
        self.matcher.remove('CONECTORES_ADVERSATIVOS_PATRON')
        self.matcher.remove('CONECTORES_CONSECUTIVOS_PATRON')
        self.matcher.remove('CONECTORES_RECAPILUTIVOS_PATRON')
        self.matcher.remove('CONECTORES_ORDENACION_PATRON')
        
        return len(reason) == 0, reason