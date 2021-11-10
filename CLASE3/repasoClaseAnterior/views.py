from django.shortcuts import render

# Create your views here.

def vistaConTemplate(request):
    return render(
        request,
        'repasoClaseAnterior/index.html',
        {"name" : "Matias"}
    )

