from django.shortcuts import render 
from AppWeb.models import Proveedor, Cliente, Item # importe los modelos de models.py
from AppWeb.forms import ProveedorFormulario, UsuarioRegistro, formularioEditarUsuario, AvatarFormulario #importe el formulario

#librerias necesarias para el manejo de sesion
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.mixins import LoginRequiredMixin  #esto se usa para la vistas de clase para impedir ver info no logueado, pero yo las vistas las hice por funcion por lo q se usa la libreria debajo
from django.contrib.auth.decorators import login_required


# Create your views here.

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

                    return render(request, "AppWeb/inicio.html", {"mensaje":f"Bienvenido {user}"})
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
            return render (request, "AppWeb/inicio.html", {"mensaje":"Usuario Creado"})
          
     else:

        form= UsuarioRegistro()
    
     return render(request, "AppWeb/registro.html", {"formulario":form})
    

@login_required #para q solo se puede entrar si se inicio cesion
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
               
               avatar= avatar(user=request.user, imagen=informacion['imagen'])
               avatar.save()

               return render(request, "AppWeb/inicio.html")
          
     else:
          
              miFormulario =AvatarFormulario() #si no q me mande el Formulario Vacio
              
     return render(request, "AppWeb/agregarImg.html", {'form':miFormulario})




#vistas de Clases

@login_required  #impide acceder si no estoy logueado
def prov (request):
    return render(request, "AppWeb/prov.html")

@login_required
def cliente (request):
    return render(request, "AppWeb/clientes.html")

@login_required
def item (request):
    return render(request, "AppWeb/items.html")



#CRUD
#Insertar datos
def agregar_prov(request):
    nuevo_formulario=ProveedorFormulario()
    if request.method == "POST":  #si el formulario tiene el metodo post q avance

       nuevo_formulario=ProveedorFormulario(request.POST)

       if nuevo_formulario.is_valid():
           
           info=nuevo_formulario.cleaned_data  #define a info como un diccionario
           
           prov_nuevo=Proveedor(nombre=info["nombre"],condicion=info["condicion"], CUIT=info["CUIT"]) #para los value tomo los nombres de la clase form y para las Key me dio error cuando lo puse en Minuscula por lo q debe tomar del nombre del  Modelo
           #esta sentencia llena a la base de datos del Modelo Proveedor asignando de forma forzoza nombre de la clase modelo = argumento del diccionario del formulario

           prov_nuevo.save()

           return render(request, "AppWeb/inicio.html") #para q me lleve a la pag de inicio luego de guadar
       

    return render(request, "AppWeb/form_prov.html", {"mi_formu":nuevo_formulario}) #a donde lleva la view




#read
def leer_prov(request):

     
        proveedores=Proveedor.objects.all()
        contexto= {"Supliers": proveedores}

        return render(request, "AppWeb/leer_prov.html", contexto )  #en este caso guardo la variable contexto como argumento q tiene el mismo efecto q ponerlo como argumento como en el caso de arriba result_prov

#alternativa a leer
def buscar_prov(request):
        
        return render(request, "AppWeb/buscar_prov.html")


def resul_prov(request):

    if request.method=='GET':

        prov_pedido=request.GET['nombr']
        resul_prov=Proveedor.objects.filter(nombre__icontains=prov_pedido) #si quiero busqueda exacta reemplazar icontains x iexact

        return render(request, "AppWeb/result_busqueda_prov.html", {"provs":resul_prov} )  #provs viene de la plantilla resultado_busqueda..
    else:
        return render(request, "AppWeb/buscar_prov.html")


#delete
def eliminar_prov(request, provNombre): #se pide por parametro el prov a eliminar
     
     prov_eliminar=Proveedor.objects.get(nombre=provNombre) #para guardar el prov a eliminar
     prov_eliminar.delete()

     prov_restantes=Proveedor.objects.all()

     contexto= {"Supliers": prov_restantes}
     
     return render(request, "AppWeb/leer_prov.html", contexto)

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
        


def about(request):
    return render(request, "AppWeb/about.html")     


     



