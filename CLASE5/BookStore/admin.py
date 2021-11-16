from django.contrib import admin
from django.contrib.admin.helpers import Fieldset
from .models import Book, Author, Editorial
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=('title', 'editorial')
    list_filter = ['title']
    fieldsets =[
        ('Datos del libro', {'fields' : ['title', 'price', 'sysnopsis', 'publish_date']}),
        ('Datos de la editorial', {'fields' : ['editorial']}),
        ('Datos de los autores', {'fields' : ['authors']}),

    ]

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Editorial)

