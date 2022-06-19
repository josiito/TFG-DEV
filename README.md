# Trabajo de Fin de Grado - Lectura fácil: validador de texto
Este repositorio almacenará todo lo relacionado, tanto código como recursos, de mi trabajo de fin de grado
titulado "Lectura fácil: validador de texto".

Además, se realizará una pequeña guía de como ejecutar la práctica, para toda persona que sienta curiosidad del funcionamiento de este trabajo.

# Introducción
Este trabajo se ha desarrollado en dos proyectos [Django](https://docs.djangoproject.com/en/4.0/). El principal motivo por el que se ha desarrollado dos proyectos en lugar de dos aplicaciones en un único proyecto (posibilidad que te da el uso del framework) es que se necesitaba tener los dos servicios activos, por lo que es necesario tener dos puertos en uso, el 8000 (por defecto de un proyecto Django) para la página web y el 8001 para la API.

Por lo tanto, tenemos dos proyectos llamados:

- __Proyecto-TFG__: es la parte principal del trabajo y en este se define todo lo relacionado al desarrollo de la API RESTful. A través de esta, se pueden obtener los resultados del análisis del texto en formato json.

- __PaginaWebTFG__: es la parte más opcional del trabajo y define la página web que consumirá la API desarrollada. En esta se pretende que el usuario tenga dos opciones de mandar el texto para que se analice con las llamadas a la API: mediante un cuadro de texto y subiendo un fichero de texto plano (con extensión txt) que contenga el texto a analizar.

# Primeros pasos
Como se está utilizando Django como framework, se utilizará [Python](https://www.python.org/downloads/) como principal lenguaje de programación y se supondrá que ya se tiene instalado. Para ejecutar el trabajo de manera correcta, es necesario tener un entorno virtual.

## Entorno virtual
El entorno virtual nos servirá para encapsular las dependencias de los proyectos que conforman este trabajo, con las versiones que utilizaré durante el desarrollo del mismo. Este se ha de inicializar al mismo nivel de los proyectos y del fichero requirements.txt. De un modo más gráfico podemos verlo como:

```
|   .gitignore
|   README.md
|   requirements.txt
|          
+---PaginaWebTFG
\---Proyecto-TFG
```

Para crear el entorno virtual de python podemos hacerlo mediante el siguiente comando (para versiones linux será necesario comenzar el comando con "python3")

```
python -m venv .env
```

Para ejecutar este entorno virtual se utiliza la siguiente linea:

Para windows:
```
.env\Scripts\activate.bat
```

Para linux:

```
source .env/Scripts/activate
```

Esto nos permitirá instalar todas las dependencias de los proyectos en nuestro entorno virtual sin afectar la instalación de python sobre otros proyectos.

## Instalación de dependencias
Una vez creado el entorno virtual de python, hay que instalar las dependencias para que los proyectos ejecuten correctamente. Esto lo conseguimos con:

```
pip install -r requirements.txt
```

Por otro lado, una de las dependencias es la libreria de procesamiento de lenguaje natural, spaCy, por lo que necesitamos instalar todo el vocabulario que utiliza esta en nuestro entorno con el siguiente comando:

```
python -m spacy download es_core_news_sm
```

Una vez instaladas todas las dependencias, ya podemos ejecutar el trabajo.

# Ejecución de la práctica
Para ejecutarla, como se ha dicho anteriormente, es necesario tener dos puertos libres, el 8000 y el 8001, para desplegar los dos proyectos de Django.

Para ello tenemos que abrir dos terminales ponernos a la altura del fichero _manage.py_ de cada proyecto y ejecutar lo siguiente:

En la terminal donde se va a desplegar la página web:

```
python manage.py runserver
```

Y, en la terminal donde se va a desplegar el servicio de la API:

```
python manage.py runserver 8001
```

De esta manera ya tendremos desplegados ambos servicios listos para usar. Para abrirlo desde el navegador se puede pinchar en la ruta que te proporciona django la desplegar la aplicación o en la siguiente ruta:

```
http://localhost:8000/
```

En la página se tienen varias entradas donde se explican las pautas que se han implementado y algunos conceptos de interés.