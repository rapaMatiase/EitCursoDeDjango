from django.shortcuts import render

# Create your views here.


def FirstView(request):
    return render(
        request,
        'RespasoClaseAnterior/index.html',
        {}
    )