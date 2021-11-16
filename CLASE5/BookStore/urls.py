from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList, name="bookList"),
    path('editorials/', views.EditorialList, name="editorialList"),
    path('authors/', views.AuthorList, name="authorList"),
    path('book/<int:id>/', views.BookDetail, name="bookDetail"),
    path('author/<int:id>/', views.AuthorDetail, name="authorDetail"),
    path('editorial/<int:id>/', views.EditorialDetail, name="editorialDetail"),

]