from django.urls import path
from .views import vistaConTemplate

urlpatterns = [
    path('index/', vistaConTemplate)
]
