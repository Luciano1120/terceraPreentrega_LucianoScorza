from django.http import HttpResponse #lo use solo para probar la hora actual. Pero no hace falta usarlo, ya q conviene usar el render
import datetime as dt #lo use solo para probar la hora actual

from django.shortcuts import render 
from AppWeb.models import Proveedor, Cliente, Item, avatar # importe los modelos de models.py
from AppWeb.forms import ProveedorFormulario, UsuarioRegistro, formularioEditarUsuario, AvatarFormulario #importa los formularios

#librerias necesarias para el manejo de sesion
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.mixins import LoginRequiredMixin  #esto se usa para la vistas de clase para impedir ver info no logueado, es como el login_required pero para clases
from django.contrib.auth.decorators import login_required #permite q solo se acceda a esa funcion vinculada a un boton estando logueado

from django.contrib.auth.models import User #para traer la clase usuario para el avatar

from django.views.generic import ListView  #la uso para las vistas de clases,para el read
from django.views.generic.edit import CreateView, UpdateView, DeleteView  #la uso para las vistas de clases para el create


# Create your views here.
def hora_actual(request):  #el parametro request es obligatorio. Lo exige django en las views por más q no se use
     ahora= dt.datetime.now()
     mensaje= f'{ahora}'
     return HttpResponse (mensaje)  #no hace falta una plantilla de HTML en este caso, aunque podría usar alguna y usarla como parametro en vez de mensaje(clase 18 min 1.21) /el HttpResponse solo lee strings


#vista de Inicio
def inicio (request):
    return render(request, "AppWeb/inicio.html")


#vista de login, register y logout

def inicioSesion(request):
     
     if request.method == "POST":    #es decir si la doy al boton..
          
          form=AuthenticationForm(request, data =request.POST)

          if form.is_valid():
               
               usuario= form.cleaned_data.get("username") #ppara llamar al value de la key del get
               Contra= form.cleaned_data.get("password") 

               user=authenticate(username= usuario, password=Contra) #para validar user y password

               if user:
                    login(request, user)

                    return render(request, "AppWeb/inicio.html", {"mensaje":f"Usuario {user}"})
               else:
                     return render(request, "AppWeb/inicio.html", {"mensaje":"Datos Incorrectos"}) 
               
     else:
          form = AuthenticationForm()

     return render (request, "AppWeb/login.html", {"formulario":form})

               
def registro(request):
     
     if request.method == "POST":
          
          form = UsuarioRegistro(request.POST)

          if form.is_valid():
            
            username= form.cleaned_data["username"]
            form.save()
            return render (request, "AppWeb/inicio.html", {"mensaje":f"Usuario {username}"})
          
     else:

        form= UsuarioRegistro()
    
     return render(request, "AppWeb/registro.html", {"formulario":form})
    

@login_required #es un decorador , para q solo se puede entrar si se inicio cesion
def editarUsuario(request):

    usuario=request.user

    if request.method == 'POST':

        form= formularioEditarUsuario(request.POST)

        if form.is_valid():
             info= form.cleaned_data  #diccionario q contiene los datos limpios

             usuario.email = info["email"]
             usuario.set_password = info["password1"]
             usuario.first_name = info["first_name"]
             usuario.last_name = info["last_name"]

             usuario.save()

             return render (request, "AppWeb/inicio.html")
    
    else:
         
         form = formularioEditarUsuario(initial={"email": usuario.email ,
                                        "first_name": usuario.first_name,
                                        "last_name":usuario.last_name})
         
    return render (request, "AppWeb/editarUsuario.html",{"formulario" : form , "usuario": usuario})



def cerrarSesion(request):
    logout(request) 

    return render (request, "appweb/logout.html")

#agregar Avatares (vista para subir imagenes)

@login_required
def agregarImagen(request):
     
     if request.method == "POST":    #es decir si la doy al boton subir imagenes q  siga con esos pasos
          
          miFormulario=AvatarFormulario(request.POST, request.FILES)

          if miFormulario.is_valid():
               
               informacion= miFormulario.cleaned_data
               usuario_actual= User.objects.get(username=request.user)
               
               avatar_nuevo= avatar(usuario=usuario_actual, imagen=informacion["imagen"])
               avatar_nuevo.save()

               return render(request, "AppWeb/inicio.html")
          
     else:
          
          miFormulario =AvatarFormulario() #si no q me mande el Formulario Vacio
              
     return render(request, "AppWeb/agregarImg.html", {'formu':miFormulario})




#vistas de Clases

@login_required  #impide acceder si no estoy logueado
def prov (request):  #esta vista ya no la estoy llamando de ningun lado, ya q estoy llamando a la vista todos_prov
    return render(request, "AppWeb/prov.html")

@login_required
def cliente (request):
    return render(request, "AppWeb/clientes.html")

@login_required
def item (request):
    return render(request, "AppWeb/items.html")




#inserta en Items Prueba simple
def agregaItemSimpleSinForm(request):
     item1=Item(nombre="Freezer1600", categoria="Freezer") #le paso los parametro para q complete a la BBDD cuando se plasme el url en el navegador
     #ho hace falta pasar el ID ya q entra solo por ser PK
     item1.save()
     return render (request, "AppWeb/agregaItemSimpleSinForm.html")


def agregaItemConForm(request):
# formulario con HTML     
     #item2=""
     if request.method == "POST":  #si no agrego este condicional cada vez q quiera hacer un POST da error
                          #es decir si hace click en el submit q avance con la ejecucion del codigo  
     
        item2=Item(
             nombre = request.POST["nombre"],
             categoria = request.POST["categoria"]
             )
     #tal cual la view de arriba acá le doy los parametros a traves de los nombres q le di a a los imput de las caja de texto

        item2.save()    

     return render (request, "AppWeb/agregaItemConForm.html")



#CRUD Provedores
#Insertar datos
#se hace con formularios de django y no como hicimos de Items arriba
def agregar_prov(request):
    nuevo_formulario=ProveedorFormulario()
    if request.method == "POST":  #si le damos click al boton de submit q avance

       nuevo_formulario=ProveedorFormulario(request.POST) #con esta linea obtenemos los datos del formulario  HTML

       if nuevo_formulario.is_valid():  #verificamos q los datos del formualario sean validos. Tipos de datos por ejemplo, si hay datos vacio, y no tengo el error q me da el agregaItemConForm q no se por que no entra en la BD
           
           info=nuevo_formulario.cleaned_data  #define a info como un diccionario, y q venga limpia
           
           prov_nuevo=Proveedor(nombre=info["nombre"],condicion=info["condicion"], CUIT=info["CUIT"]) 
           #esta sentencia llena a la base de datos (Modelo Proveedor) asignando de forma forzoza nombre de la clase modelo = argumento del diccionario del formulario
           #para el diccionario info se ponen las key q son los Atributos del Formulario
           

           prov_nuevo.save()

           return render(request, "AppWeb/inicio.html") #para q me lleve a la pag de inicio luego de guardar- a esta pagina me lleva luego de guardar, la q está debajo es donde me ubico antes
        
        #no me hace falta este else para q cuando se ubique en la url aparezca vacio el formulario
        #else: 
         #   nuevo_formulario=ProveedorFormulario() """

    return render(request, "AppWeb/agregaProv.html", {"mi_formu":nuevo_formulario}) #recibe 3 argumentos (request obligado- el html - el contexto (permite la vinculacion con el HTML))
    #este return es donde me situa el navegador cuando se llama a la vista desde la url




#read
def leer_prov(request):

     
        proveedores=Proveedor.objects.all()  #obtengo todos los registros de la clase o modelo Proveedor. Guardo en una variable proveedores todos los registros accediendo a la clase Proveedor con el metodo .objects.all()
        contexto= {"Supliers": proveedores} #guardo los registro en un diccionario

        return render(request, "AppWeb/leer_prov.html", contexto )  #en este caso guardo la variable contexto (es un diccionario) como argumento q tiene el mismo efecto q ponerlo como argumento como en el caso de arriba result_prov. es lo q le voy a pasar al HTML para q lea a través de la Key del diccionario (Supliers)



#muestro a todos los Proveedores
@login_required
def todos_prov(request):
        
        proveedores=Proveedor.objects.all()  #obtengo todos los registros de la clase o modelo Proveedor. Guardo en una variable proveedores todos los registros accediendo a la clase Proveedor con el metodo .objects.all()
        contexto= {"Supliers": proveedores} #guardo los registro en un diccionario, ver debajo como sería el diccionario en un ejemplo

        """  es importante la indentation de la triple comilla para q no se error
            por otro lado vemos como sería el diccionario de la variable contexto
        {
    'Supliers': [
        {'nombre': 'Proveedor A', 'direccion': 'Dirección A', 'telefono': '123-456-789'},
        {'nombre': 'Proveedor B', 'direccion': 'Dirección B', 'telefono': '987-654-321'}
    ]
}
        """

        return render(request, "AppWeb/prov.html", contexto )  #en este caso guardo la variable contexto (es un diccionario) como argumento q tiene el mismo efecto q ponerlo como argumento como en el caso de arriba result_prov. es lo q le voy a pasar al HTML para q lea a través de la Key del diccionario (Supliers)

    
#alternativa a leer-----------------------------
def buscar_prov(request):
        
        return render(request, "AppWeb/buscar_prov.html")
#Complementa a buscar_prov
def resul_prov(request):

    if request.method=='GET':  #si se le hace click al boton buscar q siga dentro del if

        prov_pedido=request.GET['nombr']  #guardamos en una variable en valor de la cajita de texto del formulario
        resul_prov=Proveedor.objects.filter(nombre__icontains=prov_pedido) #para filtrar lo q pidio el usuario en la variable de arriba - si quiero busqueda exacta reemplazar icontains x iexact

        return render(request, "AppWeb/result_busqueda_prov.html", {"provs":resul_prov} )  #provs es lo que le paso a la plantilla HTML para q muestre los datos
    else:
        return render(request, "AppWeb/buscar_prov.html")

#----------------------------------------------------------------------


#delete
def eliminar_prov(request, provNombre): #se pide por parametro el prov a eliminar
     
     prov_eliminar=Proveedor.objects.get(nombre=provNombre) #para guardar el prov a eliminar
     prov_eliminar.delete()

     prov_restantes=Proveedor.objects.all()

     contexto= {"Supliers": prov_restantes} 
     
     return render(request, "AppWeb/leer_prov.html", contexto) #el argumento contexto del render debe ser un diccionario, y es de la forma en q se le pasa al HTML una variable. Se le debe pasar la "Key" del diccionario como variable dentro de dobles llaves {{}} (similar al f string para leer variables dentro de cadenas de texto)

#update
def editarProv(request, provNombre):
    nuevo_formulario=ProveedorFormulario() 
    prov_edit=Proveedor.objects.get(nombre=provNombre) 

    if request.method == "POST": #si se le da click a boton editar 

        nuevo_formulario=ProveedorFormulario(request.POST)

        if nuevo_formulario.is_valid():
           
           info=nuevo_formulario.cleaned_data  #define a info como un diccionario
           
           prov_edit.nombre = info["nombre"]  #se asigna los atributos de la clase instancia en un nuevo objeto prov_edit con lo q se completa del formulario
           prov_edit.CUIT = info["CUIT"]
           prov_edit.condicion = info["condicion"]
           

           prov_edit.save() #para guardar los datos en el nuevo objeto de clase proveedor

           return render(request, "AppWeb/inicio.html") #luego de guardar muestra la pantalla de Inicio
        
    else :
            nuevo_formulario = ProveedorFormulario (initial= {"nombre": prov_edit.nombre, 
                                                              "CUIT": prov_edit.CUIT, 
                                                              "condicion": prov_edit.condicion}) 
            #initial para q aparezcan los valores iniciales q tiene dicho proveedor


    return render (request, "AppWeb/formEditarProv.html", {"mi_formu": nuevo_formulario, "nombre":provNombre })    
        
#-------------------------------------------------

#CRUD de Items con vista de clases


class ListaItem(LoginRequiredMixin,ListView): #creamos una clase q hereda de ListView q es la libreria importada  / LoginRequiredMixin es para q no permita el acceso al boton si no inicio sesion
    model= Item  #importamos el modelo/clase pelicula
    #el html se tiene q llamar igual al objeto instanciado  Item_list.html para q django la renocozca automaticamente y la vincule con la vista basada en clases


class CreaItem(CreateView): #creamos una clase q hereda de ListView q es la libreria importada  
    model= Item  #importamos el modelo/clase pelicula
    

    fields=["id", "nombre", "categoria"]  #campos a agregar registos q vienen del modelo
    success_url = "/AppWeb/listaItem/"  #necesario para direccionar a q pagina me tiene q llevar
    #usa el por default el template item_form.html

class ActualizaItem(UpdateView): #creamos una clase q hereda de ListView q es la libreria importada  
    model= Item  

    fields=["id", "nombre", "categoria"]  #campos a agregar registos q vienen del modelo
    success_url = "/AppWeb/listaItem/"  #necesario para direccionar a q pagina me tiene q llevar
    #usa el mismo template del create

class BorrarItem(DeleteView): #creamos una clase q hereda de ListView q es la libreria importada  
    model= Item  

    success_url = "/AppWeb/listaItem/"  #necesario para direccionar a q pagina me tiene q llevar
    #usa el por default el template item_confirm_delete.html




#--------------------------------------------------

def about(request):
    return render(request, "AppWeb/about.html")     


     



