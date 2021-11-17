from django.shortcuts import render
from .models import News, Journalist
# Create your views here.
def Index(request):
    """
        Al entrar al index vamos a ver las ultimas noticias.
    """
    return render(
        request,
        'NewsPaperApp/index.html',
        {}
    )

def ListNews(request):
    query = News.objects.all().order_by('publish_date')
    return render(
        request,
        'NewsPaperApp/list-news.html',
        {"list" : query}
    )

def DetailNews(request, id):
    query = News.objects.get(id=id)
    return render (
        request,
        'NewsPaperApp/detail-news.html',
        {'new' : query}
    )