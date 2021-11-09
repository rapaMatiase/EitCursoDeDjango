"""CLASE2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Como importo las vistas?
# Aca importo todo lo que tiene el archivo.
from repasoClaseAnterior import views 
#Aca importando solo la funcion VistaSimple
from repasoClaseAnterior.views import VistaSimple 

urlpatterns = [
    path('admin/', admin.site.urls),
    #Estoy incluyento todas las urls del archivo urls de la app repasoClaseAnterior.
    path('repaso/', include('repasoClaseAnterior.urls'))
    #La linea de arriba equivale a 
    # path('admin/', admin.site.urls),
    # path('intento1/', views.VistaSimple),

]
