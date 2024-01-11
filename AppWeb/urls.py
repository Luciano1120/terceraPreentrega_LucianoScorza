#este archivo urls.py dentro de la AppWeb se creo y se copio tal cual del archivo urls.py de Proyecto

from django.urls import path
from AppWeb.views import *


urlpatterns = [
    path("", inicio, name='inicio'),  #con solo poner http://127.0.0.1:8000/AppWeb/ ya sale 
    
    #para modelos
    path("items/", item, name='item'), # 1er argumento para la continuacion del path de la url- 2do toma de la view - 3ro referencia para boton HTML del padre.html
    path("clientes/", cliente, name='cliente'),
    path("prov/", prov, name='prov'),

    path("pruebas/", prueba),

    #para nuevos datos
    path("nuevoprov/", agregar_prov),

    #para buscar datos
    path("buscaprov/", buscar_prov),
    path("resultprov/", resul_prov),


]
