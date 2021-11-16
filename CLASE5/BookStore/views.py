from django.db.models.query_utils import Q
from django.shortcuts import render
from .models import Book, Author, Editorial
# Create your views here.


def BookList(request):
    #Esto me trea una lista con todos los libros en BD.
    query = Book.objects.all()
    return render(
        request,
        'BookStore/book-list.html',
        { 'bookList' : query}
    )

def BookDetail(request, id):
    #El primer id es el campo en base de datos, y el segundo es el parametro que recibi.
    query = Book.objects.get(id=id)
    return render(
        request,
        'BookStore/book-detail.html',
        { 'book' : query}
    )

def AuthorList(request):
    query = Author.objects.all()
    return render(
        request,
        'BookStore/author-list.html',
        { 'authorList' : query}
    )

def AuthorDetail(request, id):
    # Se puede utilizar get o filter
    query = Author.objects.get(id=id)
    return render(
        request,
        'BookStore/author-detail.html',
        { 'author' : query}
    )

def EditorialList(request):
    query = Editorial.objects.all()
    
    return render(
        request,
        'BookStore/editorial-list.html',
        {'editorialList' : query}
    )

def EditorialDetail(request, id):
    query = Editorial.objects.get(id=id)
    return render(
        request,
        'BookStore/editorial-detail.html',
        {'editorial' : query}
    )