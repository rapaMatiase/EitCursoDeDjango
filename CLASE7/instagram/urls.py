from django.urls import path
from .views import Home, Detial, Perfil

urlpatterns = [
    path(
        'home/<int:user_id>/', 
        Home, 
        name="home"
        ),
    path(
        'detail/<int:post_id>/', 
        Detial, 
        name="detail"
    ),
    path(
        'perfil/<int:user_id>/',
        Perfil,
        name='profile'
    )
]