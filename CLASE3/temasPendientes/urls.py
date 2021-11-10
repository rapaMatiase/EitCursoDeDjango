from django.urls import path
from .views import index, aboutUs, contact

urlpatterns = [
    path('', index, name='index'),
    path('about/', aboutUs, name='about'),
    path('contact/', contact, name='contact')
]

"""
Ejercicio 2 

Agregar un nombre a cada url en el app de temasPendientes y crear en el index.html un url para ir a about y contact.

Tambien crear las urls necesarias para ir de about a contact y index. Por ultimo de contact a index y aobut. 

3 min 11.15Am
"""