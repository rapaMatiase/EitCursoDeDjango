from django.urls import path
from . import views

urlpatterns = [
    path('', views.FirstView, name="first"),
    path('second/<str:name>/', views.SecondView, name="second"),
    path('studentList/', views.StudentList, name="StudentList"),
    path('studentDetail/<int:id>/', views.StudentDetail, name="StudentDetail")
]