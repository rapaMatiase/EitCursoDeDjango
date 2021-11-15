from django.urls import path
from . import views

urlpatterns = [
    path(
        'list/',
        views.BookList,
        name="BookList"
        ),
    path(
        'detail/',
        views.BookDetail,
        name="BookDetail"
    )
]