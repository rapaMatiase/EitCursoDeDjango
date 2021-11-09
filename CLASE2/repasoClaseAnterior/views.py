from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def VistaSimple(request):
    return HttpResponse("Hola, esta es la vista mas simple posible!!")
    
""" 
Ejercicio 1
Crear una vista que diga "Hola, como estas?" en el navegador.
2min 11.28AM
"""

def Saludar(request, name):
    return HttpResponse("Hola " + name + ", como estas?")

def SaludarMultiplesPersonas(request, name1, name2, age):
    return HttpResponse("Hola " + name1 + " , " + name2  )

"""
Ejercicio 2
Crear una vista que reciba el nombre, apellido y edad de un usuario y lo muestre en pantalla.
2 min 11.40AM
"""

def SaludoCompleto(request, name, lastName, age):
    return HttpResponse("Hola {1}, {0} con edad {2}".format(name, lastName, age))

def UsoDelHtmlConMalasPracticas(request):
    return HttpResponse("""
        <h1> Titulo <h2>
        <p style="color:blue;"> Este es un parrafo de ejemplo </p>
    """)
    # La mala practica esta en que tengo codigo de HTML envevido en codigo de Python. --> Injeccion de codigo

def usoCorrectoDeUnHtml(request):
    #return render(request, 'carpeta_nombre_app/template.html')
    return render(request, 'repasoClaseAnterior/index.html')

def cargarHtmlConContexto(request):
    #return render(request, 'carpeta_nombre_app/template.html', context={ es un diccionario !!!})
    return render(
        request, 
        'repasoClaseAnterior/indexWithContext.html',
        {
            "name" : "Matias", 
            "lastName" : "Rapa",
            "status" : "al dia",
            "Pendientes" : [
                "Comprar tomate",
                "Lavar la ropa",
                "Sacar al perro",
                "Estudia django"
            ]
        })


""" 
Ejercicio 3
Crear una vista con template que reciba por la url el nombre, apellido y emosion del usuario.
Mostra en el HTML el nombre y aprellido de color verde si la emosion es felicidad, si no de color rojo si es enojado. Por ultimo, si es triste de color azul.
3min 12.44AM 
 """

def ejercicio3(request, name, lastName, feeling):
    return render(
        request,
        'repasoClaseAnterior/ejercicio3.html',
        {
            "name" : name,
            "lastName" : lastName,
            "feeling" : feeling
        }
    )

"""
Ejercicio 4

Dada una lista de diccionarios. Mostrar en pantalla en formato de lista con el elemento Ul. Si el estado es ok, mostrar de color verde, si el estado es no ok, mostrar de color rojo.
4 min 13.03PM
"""

lista = [
    {"name":"tomate", "status": "ok"},
    {"name":"Cocacola", "status": "nook"},
    {"name":"Lechuga", "status": "ok"},
    {"name":"Manzana", "status": "ok"}
    ]

def ejercicio4(request):
    
    return render(
        request,
        'repasoClaseAnterior/ejercicio4.html',
        {"lista": lista}
    )