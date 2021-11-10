# EitCursoDeDjango
Material realizado durante el curso de Django en Educacion it

# Clase 1

Crear un entrono virtual para trabajar.

    py -m venv <nombre_del_entrono_virtual>

Los tipicos nombres que se utilizan son .env y .venv, y si con un punto al frente para que sea una carpeta oculta. 

Despues hay que activarlo para comenzar a trabjar.

    source <nombre_entorno>/bin/activate (Linux o Mac)
    source <nombre_entorno>/Scripts/activate (Windows)

Ya con el entorno virtual activado, necesito intalar los paquetes para trabajar. Puedo tener dos situaciones en este cos;

* Es un proyecto nuevo, tengo que intalar cada paquete por separado utilizando el comando de 
    pip intall <nombre_del_paquete>

* Es un proyecto ya existente, y tengo que intalar el archivo requiremts.txt.

    pip install -r requirements.txt

Crear un nuevo proyecto de django para trabajar. El ejecutar el siguiente comando no devulve ningun mensaje por consola en coso de ejecutarse exitosamente, pero si crea una carpeta nueva en el directorio donde se ejecuto.

    django-admin startproject <nombre_proyecto>

Despues de crear el nuevo proyecto para continuar trabajando necesito moverme adentro de la carpeta del mismo.

    cd <nombre_Del_proyecto>

Ahora creamos una app (esto representa un servicio que vamos a otorgar en nuestra pag). Recordatorio, esto hay que ejecutarlo en la misma ubicacion que el archivo 'manage.py' siempre (Podemos chequear eso con el comando 'ls').

    python manage.py startapp <nombre_de_la_app>

Si este comando esta ejecutado correctamente, no deuvleve ningun mensaje por consola, pero crea una carpeta nueva en esa ubicacion. 

Cosas que debo hacer despeus de crear una app nueva:
* Agregar la app en la lista de INSTALL_APPS en setings.py en la carpeta del proyecto. 
* Utilizar la funcion include para incluir las urls de mi app, y crear un archivo propio de urls en la app.

## ¿Como creo la respuesta mas sencilla posible?

Primero creamos una vista, que puede ser una funcion o una clase, en el archivo de views.py en nuestra App. Necesitamos importer HttpResponse

    from django.http import HttpResponse

Ahora podemos crear una vista con una funcion y el HttpResponse.

Lo segundo a hacer es craer la url para acceder a esa vista. Esta url peude esta ubicada en dos lugares:
* Urls.py del poryecto.
* Para mas despues
