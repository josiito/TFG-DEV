from django.http import HttpRequest
from django.shortcuts import render
from django.core.files import uploadedfile

import json
import requests

BASE_URL_API   = 'http://127.0.0.1:8001/api/'
PAUTAS_URL = [ 
    BASE_URL_API + 'comp/cont-indet/',
    BASE_URL_API + 'comp/num-tlf/',
    BASE_URL_API + 'comp/form-hora/',
    BASE_URL_API + 'comp/conec-comp/',
]

PAUTA_DESC = [
    'Palabra de contenido indeterminado',
    'Numero de telefono mal formateado',
    'Formato de hora incorrecta',
    'Conectores complejos',
]

def main(request: HttpRequest):
    return render(request, 'index.html')

def info(request: HttpRequest):
    return render(request, 'informacion.html')

def acerca_de(request: HttpRequest):
    return render(request, 'acerca-de.html')

def resultado(request: HttpRequest):
    if request.method == 'POST':

        # Obtenemos la pauta del desplegable con nombre = 'lista-de-pautas'
        # y la url de la peticion con el valor del campo anterior (mirar html).
        pauta = request.POST['lista-de-pautas']
        url_peticion = PAUTAS_URL[int(pauta)]
        
        # Se ha enviado un fichero para analizar su contenido
        if (content_type := request.content_type) == 'multipart/form-data':
            file: uploadedfile = request.FILES['td-field']
            texto = file.read().decode('utf-8')

            response = requests.post(url_peticion, json = json.dumps({'documento': texto}))
            result = json.loads(response.text)

            if response.status_code == 200:
                if result['correccion']:
                    return render(request, 'resultado.html', context = {
                        'passed': result['passed'],
                        'reasons': result['reason'],
                        'pauta': PAUTA_DESC[int(pauta)],
                        'correccion': result['correccion'],
                    })

                return render(request, 'resultado.html', context = { 
                    'passed': result['passed'],
                    'reasons': result['reason'],
                    'pauta': PAUTA_DESC[int(pauta)],
                })
            else:
                return render(request, 'resultado.html', context={'error': result['error']})

        # Se ha enviado texto plano para analizar su contenido
        if content_type == 'application/x-www-form-urlencoded':
            text_content = request.POST['td-field']

            response = requests.post(url_peticion, json=json.dumps({'documento': text_content}))
            result = json.loads(response.text)

            if response.status_code == 200:
                if result['passed']:
                    return render(request, 'resultado.html', context={
                        'passed': result['passed'],
                    })
                else:
                    if result['correccion']:
                        return render(request, 'resultado.html', context = {
                            'passed': result['passed'],
                            'reasons': result['reason'],
                            'pauta': PAUTA_DESC[int(pauta)],
                            'correccion': result['correccion'],
                        })

                    return render(request, 'resultado.html', context = { 
                        'passed': result['passed'],
                        'reasons': result['reason'],
                        'pauta': PAUTA_DESC[int(pauta)],
                    })

            else:
                return render(request, 'resultado.html', context={'error': result['error']})
    
    # Caso de get
    return render(request, 'resultado.html')
