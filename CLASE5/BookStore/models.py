from django.db import models

# Create your models here.

class Editorial(models.Model):
    name = models.CharField(max_length=150)
    adress = models.CharField(max_length=400)

    def __str__(self):
        return "{0}".format(self.name)

class Author(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    def __str__(self):
        return "{0}, {1}".format(self.lastname, self.name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    sysnopsis = models.CharField(max_length=300)
    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.CASCADE
    )
    authors = models.ManyToManyField(Author)
    price = models.IntegerField(default=0)
    publish_date = models.DateTimeField(default=None, null=True)
    #authors = models.ManyToManyField(Author, through='Entidad extra')

    def __str__(self):
        return "{0}".format(self.title)

# class EntidadExtra():
#     Definir campos extra para esa tabla. 
