from django.shortcuts import render

# Create your views here.

""" Esto por ahora es una base de datos improvisada """
baseDeDatosImprovisada = [
    {
        "id" : 1,
        "name" : "Deycis",
        "lastName" : "Mejias",
        "number" : 2
    },
    {
        "id" : 2,
        "name" : "Federico",
        "lastName" : "Sodo",
        "number" : 8
    },
    {
        "id" : 3,
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

def SearchStudent(id):
    studentFind = ""
    for student in baseDeDatosImprovisada:
        if student["id"]== id:
            studentFind = student
    return studentFind

def StudentDetail(request, id):
    print(id)
    # Una consulta de bd por un estudiante en particualr.
    student = SearchStudent(id)
    return render(
        request,
        'RespasoClaseAnterior/student-detail.html',
        {'student' : student}
    )