from django.urls import path
from .views import VistaSimple, Saludar, SaludarMultiplesPersonas, SaludoCompleto, UsoDelHtmlConMalasPracticas, usoCorrectoDeUnHtml, cargarHtmlConContexto

urlpatterns = [
    path('intento1/', VistaSimple),
    path( 'saludar/<str:name>', Saludar),
    path('saludoMultiple/<str:name1>/<str:name2>/<int:age>', SaludarMultiplesPersonas),
    path('saludoCompleto/<str:name>/<str:lastName>/<int:age>/', SaludoCompleto),
    path('malaPractica/', UsoDelHtmlConMalasPracticas),
    path('buenaPractica/', usoCorrectoDeUnHtml),
    path('contexto/', cargarHtmlConContexto)

]