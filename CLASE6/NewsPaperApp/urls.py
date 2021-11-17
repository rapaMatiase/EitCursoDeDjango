from django.urls import path
from . import views
urlpatterns = [
    path(
        '', 
        views.Index,
        name="index"
    ),
    path(
        'list/', 
        views.ListNews,
        name="listNews"
    ),
    path(
        'detail/<int:id>/', 
        views.DetailNews,
        name="detailNew"
    ),
]