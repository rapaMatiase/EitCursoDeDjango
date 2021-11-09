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