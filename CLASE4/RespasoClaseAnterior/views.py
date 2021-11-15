from django.shortcuts import render

# Create your views here.

""" Esto por ahora es una base de datos improvisada """
baseDeDatosImprovisada = [
    {
        "name" : "Deycis",
        "lastName" : "Mejias",
        "number" : 2
    },
    {
        "name" : "Federico",
        "lastName" : "Sodo",
        "number" : 8
    },
    {
        "name" : "Matias",
        "lastName" : "Rapa",
        "number" : 4
    }
]

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

def StudentList(request):
    """
        En esta vista envio todos los estudiantes.
    """
    return render(
        request,
        'RespasoClaseAnterior/student-list.html',
        {'studentList' : baseDeDatosImprovisada }
    )