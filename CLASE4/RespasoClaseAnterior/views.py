from django.shortcuts import render

# Create your views here.


def FirstView(request):
    return render(
        request,
        'RespasoClaseAnterior/index.html',
        { "nombre" : "Matias"}
    )

def SecondView(request, name):
    return render(
        request,
        'RespasoClaseAnterior/index.html',
        { "nombre" : name}
    )