from django.shortcuts import render, redirect
from . import forms
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
    #Creo una instancia de mi formulario!!
    form = forms.FormularioDeContacto()
    
    if request.method == "POST":
        form = forms.FormularioDeContacto(request.POST)
        if form.is_valid():
            return redirect('index')
        else:
            return render(
            request,
            'temasPendientes/contact.html',
            {'form' : form, 'error' : 'Hay un error'}
        )


    return render(
        request,
        'temasPendientes/contact.html',
        {'form' : form}
    )



def quejas(request):

    form = forms.FormularioDeQuejas()

    #Si es POST
    if request.method == 'POST':
        #Me saque la informacion del mensaje
        form = forms.FormularioDeQuejas(request.POST)
        #Valido que la informacion llegada cumple con lo descripto en fomrs.py
        if form.is_valid():
            print("TODO OK")

    return render(
        request,
        'temasPendientes/quejas.html',
        {'form': form}
    )

    """ 
    Ejericicio 3

    Crear un vista con formulario y html propio que sea para hacer un login.
    
    charField
    charPassowrd
    
    4min 12.44AM
    
    """