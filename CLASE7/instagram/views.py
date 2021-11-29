from django.shortcuts import render
from .models import Post, User, Comment
# Create your views here.
from .forms import CommentForm

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

def Detial(request, post_id):
    post = Post.objects.get(id=post_id)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            #Habiendo logrado guardar el comentario, creo una nueva instancia del formulario vacia!
            form = CommentForm()

    return render(
        request,
        'instagram/detail.html',
        {'post' : post, 'form' : form }
    )