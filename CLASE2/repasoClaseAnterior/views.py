from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def VistaSimple(request):
    return HttpResponse("Hola, esta es la vista mas simple posible!!")
    