from django.urls import path
from . import views

urlpatterns = [
    path('', views.FirstView),
    path('second/<str:name>/', views.SecondView)
]