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
    
def AuthorList(request):
    query = Author.objects.all()
    return render(
        request,
        'BookStore/author-list.html',
        { 'authorList' : query}
    )

def EditorialList(request):
    query = Editorial.objects.all()
    return render(
        request,
        'BookStore/editorial-list.html',
        {'editorialList' : query}
    )