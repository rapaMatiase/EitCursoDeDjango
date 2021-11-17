from django.db import models
from django.db.models.fields import CharField

# Create your models here.

"""
NO, VAMOS VOLVER DESPUES ACA.
"""

class Theme(models.Model):
    name = models.CharField(max_length=30)

class Journalist(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    thems = models.ManyToManyField(Theme)
    # image_profile= ""

class News(models.Model):
    state_of_news = [
        ("E", "Editando"),
        ("P", "Publicado"),
        ("B", "Bloqueado")
    ]

    state = models.CharField(
        max_length=2,
        choices=state_of_news,
        default="E"
    )
    create_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(null=True)
    last_update_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=300)
    write_by = models.ForeignKey(
        Journalist,
        on_delete=models.CASCADE
    )
    #imagen = ""