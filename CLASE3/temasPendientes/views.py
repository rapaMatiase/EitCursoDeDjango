from django.shortcuts import render

# Create your views here.

def index(request):
    return render(
        request,
        'temasPendientes/index.html',
    )


""" 
Ejercicio 1
Crear 2 vistas con sus propios templates con los nombres;
- Contact
- Abous us
3 min 10.50
"""

def aboutUs(request):
    return render(
        request,
        'temasPendientes/aboutus.html',
    )

def contact(request):
    return render(
        request,
        'temasPendientes/contact.html'
    )