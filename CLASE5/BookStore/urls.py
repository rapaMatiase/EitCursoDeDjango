from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList, name="bookList"),
    path('editorials/', views.EditorialList, name="editorialList"),
    path('authors/', views.AuthorList, name="authorList"),

]