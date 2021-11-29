from django.urls import path
from .views import Home

urlpatterns = [
    path('home/<int:user_id>/', Home, name="home")
]