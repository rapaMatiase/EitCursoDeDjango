from django.shortcuts import render
from .models import Post, User
# Create your views here.


def Home(request, user_id):
    # Primero instancio el usuario al que le corresponde el id
    user = User.objects.get(id=user_id)
    # Con esa instancia puedo hacer consultas
    posts = Post.objects.filter(user=user)
    return render(
        request,
        'instagram/home.html',
        {'posts' : posts }
    )