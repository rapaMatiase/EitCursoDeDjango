from django.shortcuts import render
  
# Create your views here.
def Saludar(request):
    return HttpResponse("Hola, como estas3🙋?")

""" 
Ejercicio 1
Crear una vista que muestre la palabra Enojado en pantalla.
1) Crear una funcion que recibe el request y retorna un HttpResponse.
2) Ir a url.py en muyproject y crear la url llamando a la funcion del punto 1.
3 min 12.31

"""

def Enojado(request):
    return HttpResponse("Estoy enojado 😠")

def Feliz(request):
    return HttpResponse("Estoy feliz 🙋")

def Triste(request):
    a = 2 + 3
    return HttpResponse("Estoy triste 😥 " + str(a))



