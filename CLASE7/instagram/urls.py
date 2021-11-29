from django.urls import path
from .views import Home, Detial

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
    )
]