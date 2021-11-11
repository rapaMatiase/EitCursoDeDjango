# EitCursoDeDjango

Material realizado durante el curso de Django en Educacion it.

## Clase 1

### Preparando el entorno de trabajo 

Una de las caracteristicas que deberia cumplir todos los proyectos de software es que deberia ser portable. Lograremos eso crear un entrono virtual para trabajar con el sigueitne comando. Si este comando no te sirve, puedes googlear 'python virtual enviroment' para buscar temas relacionados. 

    py -m venv <nombre_del_entrono_virtual>

Ejmplos clasicos de nombres de entornos virutales son .env y .venv, y si con un punto al frente para que sea una carpeta oculta. Si buscas dentro del archivo .gitignore podras ver otros nombre de entornos virutales y si queres otro nombre, no hay problema pero no olvides agregarlo en el .gitignore porque no se debe subir al repositorio. 

    py -m venv .env
    
Una vez creado el entorno virutal para trabajr, es necesario activarlo. Estando utilizando una consola de git bash en Windows o cualqueir consola en una distribucion de Linux o en una Mac puedes ejecutar el siguiente comando.

Si estas utilizando Linux o Mac
    
    source <nombre_entorno>/bin/activate
Si estas utilizando Windows
    
    source <nombre_entorno>/Scripts/activate

Si utilizaste el nombre de entorno virutal sugerido antes, entonces ejecuta el siguiente comando segun el sistemas operativo donde estas trabanado.

Si estas utilizando Linux o Mac
   
    source .env/bin/activate
    
Si estas utilizando Windows
    
    source .env/Scripts/activate (Windows)

Una vez activado el entonro virtual deberias poder ver entre parentesis el nombre del virtual antepuesto al la ubicacion donde estas trabajando en la consola. Ahora podemos empezar a instalar los paquetes de Python que necesitemos para trabajar sabiendo que estos se intalan en el entorno virtual y por lo tanto no afecta el funcionamiento de nuestra computadora, sea programas que tengamos intalados o otros proyectos en los que estemos trabajando. 

Es un proyecto nuevo, tengo que intalar cada paquete por separado utilizando el comando de 
    
    pip intall <nombre_del_paquete>

Es un proyecto ya existente, y tengo que intalar el archivo requiremts.txt.
    
    pip install -r requirements.txt

### ¿Como confirmo si mis paquetes estan intalados?

Podemos ejecutar la siguiente comando para ver los paquetes intalados en el entorno virtual o en global en la computadora.

    pip freeze
    
### ¿Como creo el archivo requirement.txt para exportar mi entorno de trabajo?

Muy sencillo, podes ejecutar el siguiente comando sin crear ningun archivo.

    pip freeze > requierement.txt
    
## Arrancamos con Django

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
