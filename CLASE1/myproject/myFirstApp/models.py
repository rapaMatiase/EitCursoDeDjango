from django.db import models

# Create your models here.

class prueba(models.Model):
    image = models.ImageField(upload_to='cars')