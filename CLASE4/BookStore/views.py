from django.shortcuts import render

# Create your views here.

json = [
    {
        "title" : "El arbol de las brujas",
        "year" : "1984",
        "author" : "Ray Bradbury",
        "synopsis" : "Relata la aventrua de cuatro niños a travez del tiempo para conocer el origen de Hallowin",
        "price" : "U$S15",
        "editorial" : "CasaDePapel",
        "stock" : 20
    },
    {
        "title" : "Las cronicas de Narnia - el leon, la bruja y el armario",
        "year" : "1950",
        "author" : "C. S. Lewis",
        "synopsis" : "Cuatro hermanos ingresas a un misterioso reino a travez de un  armario para convertirse en reyes y luego volver a ser mocosos sin poder",
        "price" : "U$S22",
        "editorial" : "Eyase",
        "stock" : 3
    },
    {
        "title" : "Dune - parte 1",
        "year" : "1945",
        "author" : "Frank Herbert",
        "synopsis" : "Describe las aventuras de un hombre en el desierto mientras intenta revolucionar el mundo en un mundo muy parecido al de star wars",
        "price" : "U$S44",
        "editorial" : "NoPede",
        "stock" : 12
    }
]

def BookList(reuqest):
    return render(
        reuqest,
        'BookStore/book-list.html',
        {}
    )

def BookDetail(request):
    return render(
        request,
        'BookStore/book-detail.html',
        {}
    )