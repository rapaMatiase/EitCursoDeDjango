from django.shortcuts import render
from .models import Post, User, Profile
# Create your views here.
from .forms import CommentForm, ProfileForm

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

def Perfil(request, user_id):
    #Cuando es get muestro lo que tengo cargado en base de datos
    if request.method == 'GET':
        #Busco la intancia del usurio
        user = User.objects.get(id=user_id)
        #Busco el pefil del usuario
        profile = Profile.objects.get(user=user)
        #Cargo el perfil del usuario en un formulario como apra uqe lo pueda modificar.
        form = ProfileForm(instance=profile)
    elif request.method == 'POST':
        #Verifico lo que me enviaron y lo guardo en base de datos. Tambien, vuelvo a cargar el html con los nuevos datos. 
        print("Pase poca aca ")
        #Cargo el perfil del usuario en un formulario como apra uqe lo pueda modificar.
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()

    return render(
        request,
        'instagram/perfil.html',
        {'form': form}
    )