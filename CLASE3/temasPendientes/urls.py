from django.urls import path
from .views import index, aboutUs, contact

urlpatterns = [
    path('', index),
    path('about/', aboutUs),
    path('contact/', contact)
]