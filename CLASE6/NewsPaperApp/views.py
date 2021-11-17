from django.shortcuts import render

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
    return render(
        request,
        'NewsPaperApp/list-news.html',
        {}
    )

def DetailNews(request):
    return render (
        request,
        'NewsPaperApp/detail-news.html',
        {}
    )