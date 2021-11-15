from django.db import models

# Create your models here.


# Lo que estamos escribiendo aca en PYTHON se va convertir en SQL o el lenguaje correspondiente al base de datos utilizada, nos es necesario expesificar varias reglas.

class Book(models.Model):
    #CharField es text corto en base de datos
    title = models.CharField(max_length=60)
    #Por ahora lo dejamos como texto despues vemos como trabajar con fechas.
    year = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    synopsis = models.CharField(max_length=200)
    price = models.IntegerField()
    editorial = models.CharField(max_length=60)
    stock = models.IntegerField()