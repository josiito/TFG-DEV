from django.http import HttpRequest
from django.shortcuts import render
from django.core.files import uploadedfile

import json
import requests

BASE_URL   = 'http://127.0.0.1:8001/api/'
PAUTAS_URL = [ 
    BASE_URL + 'comp/cont-indet/',
    BASE_URL + 'comp/num-tlf/',
    BASE_URL + 'comp/form-hora/',
    BASE_URL + 'comp/conec-comp/',
]

def main(request: HttpRequest):
    context = dict()

    # Caso de post
    if request.method == 'POST':

        pauta = request.POST['lista-de-pautas']
        url_peticion = PAUTAS_URL[int(pauta)]
        
        # Se ha enviado un fichero para analizar su contenido
        if (content_type := request.content_type) == 'multipart/form-data':
            file: uploadedfile = request.FILES['td-field']
            texto = file.read().decode('utf-8')

            response = requests.post(url_peticion, json = json.dumps({'documento': texto}))
            if response.status_code == 200:
                result = json.loads(response.text)

                return render(request, 'index.html', context = { 
                    'passed': result['passed'],
                    'reasons': result['reason'],
                    'response': response.text,
                })
            else:
                return render(request, 'index.html', context = {'error': 'Ha ocurrido un problema'})

        # Se ha enviado texto plano para analizar su contenido
        if content_type == 'application/x-www-form-urlencoded':
            text_content = request.POST['td-field']
            response = requests.post(url_peticion, json=json.dumps({'documento': text_content}))

            if response.status_code == 200:
                result = json.loads(response.text)

                return render(request, 'index.html', context = {
                    'passed': result['passed'], 
                    'reasons': result['reason'], 
                    'response': response.text
                })
            else:
                return render(request, 'index.html', context={'error': 'Ha ocurrido un problema'})
    
    # Caso de get
    return render(request, 'index.html')

def info(request: HttpRequest):
    return render(request, 'informacion.html')

def acerca_de(request: HttpRequest):
    return render(request, 'acerca-de.html')
