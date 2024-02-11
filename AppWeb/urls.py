#este archivo urls.py dentro de la AppWeb se creo y se copio tal cual del archivo urls.py de Proyecto

from django.urls import path
from AppWeb.views import *



urlpatterns = [
    path("", inicio, name='inicio'),  #con solo poner http://127.0.0.1:8000/AppWeb/ ya sale 
    
    path("ahora/",hora_actual),

    #para modelos
    path("items/", item, name='item'), # 1er argumento para la continuacion del path de la url- 2do toma de la view - 3ro referencia para boton HTML del padre.html
    path("clientes/", cliente, name='cliente'), #no es obligario termina con / pero es buena practica
    path("prov/", todos_prov, name='prov'),  #el name es para llamar a dicha url desde el Boton de la plantilla prov.html


    
    #para buscar datos
    path("buscaprov/", buscar_prov),
    path("resultprov/", resul_prov),
    path("todosprov/", todos_prov),  #se usa el path prov/  este path no tendría sentido pero está funcionando

    #agrega un Item sin Formulario
    path("agregaItemSimpleSinForm/", agregaItemSimpleSinForm),
    path("agregaItemConForm/", agregaItemConForm),
    
    #CRUD Proveedores con vistas basadas en funciones
    path("leerProv/", leer_prov, name="editProv"),
    
    path("agregaProv/", agregar_prov, name="agrega prov"), #es case sensitive. En el navegador lo tengo q escribir tal cual- el name se lo doy para llamarlo desde el Boton del html prov.html "Agregar Nuevo Prov"

    
    path("elimProv/<provNombre>", eliminar_prov, name="EliminarProv"),  #<provNombre> es el parametro q pide la vista q se pasa en el HTML--el name es para linkear con el buton, es decir para q dicha URL pueda ser llamada desde un Boton- la llamo desde el Boton en el html leerProv.html

    path("editProv/<provNombre>", editarProv, name="EditarProv"), #la llamo desde el Boton en el html leerProv.html

    #CRUD Item con vistas basados en Clase
    path("listaItem/", ListaItem.as_view(), name="b_item"), # a diferencia de las views basadas en funciones de agrega el nombre de la clase.as_view()
    path("agregaItem/", CreaItem.as_view(), name="a_item"), 
    path("actualizaItem/<int:pk>", ActualizaItem.as_view(), name= "e_item"),  #le tengo q poner el paramentro del id del Item en este caso el id 3 http://127.0.0.1:8000/AppWeb/actualizaItem/3
    path("borraItem/<int:pk>", BorrarItem.as_view()),

    
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
