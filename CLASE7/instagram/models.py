from django.db import models
from django.db.models.base import ModelState
from django.utils.translation import deactivate
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    detail = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)


class Post(models.Model):
    #El id que lo agrega por defualt el ORM
    detail = models.CharField(max_length=100)
    imgae = models.ImageField(null=True)
    publish_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.id)

class Comment(models.Model):
    detail = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, default=None, null=True, on_delete=models.CASCADE)

""" class Friendly(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.ForeignKey(User, on_delete=models.CASCADE) """