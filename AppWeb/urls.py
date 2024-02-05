#este archivo urls.py dentro de la AppWeb se creo y se copio tal cual del archivo urls.py de Proyecto

from django.urls import path
from AppWeb.views import *



urlpatterns = [
    path("", inicio, name='inicio'),  #con solo poner http://127.0.0.1:8000/AppWeb/ ya sale 
    
    path("ahora/",hora_actual),

    #para modelos
    path("items/", item, name='item'), # 1er argumento para la continuacion del path de la url- 2do toma de la view - 3ro referencia para boton HTML del padre.html
    path("clientes/", cliente, name='cliente'),
    path("prov/", prov, name='prov'),  #no es obligario termina con / pero es buena practica


    
    #para buscar datos
    path("buscaprov/", buscar_prov),
    path("resultprov/", resul_prov),
    path("todosprov/", todos_prov),

    #agrega un Item sin Formulario
    path("agregaItemSimpleSinForm/", agregaItemSimpleSinForm),
    path("agregaItemConForm/", agregaItemConForm),
    
    #CRUD Proveedores
    path("leerProv/", leer_prov),
    
    path("agregaProv/", agregar_prov), #es case sensitive. En el navegador lo tengo q escribir tal cual

    
    path("elimProv/<provNombre>", eliminar_prov, name="EliminarProv"),  #<provNombre> es el parametro q pide la vista q se pasa en el HTML--el name es para linkear con el buton, es decir para q dicha URL pueda ser llamada desde un Boton

    path("editProv/<provNombre>", editarProv, name="EditarProv"),

    #login
    path("login/", inicioSesion, name="Login") , 
    path("registro/", registro, name="SignUp") , 

    path("logout/", cerrarSesion, name="Logout"),  #name es para referenciarlo en el html padre dentro del boton
    path("editar/", editarUsuario, name="EditarUsuario"), #el profe trata de diferenciar el name del nnombre de la vista  

    #acerca de mi
    path("about/", about, name="acercaDeMi"), 

    #imagenes (avatar)
    path("agregarImagen/", agregarImagen, name="Agregar Imagen"), 

]
