from django.shortcuts import render
from AppWeb.models import Proveedor, Cliente, Item # importe los modelos de models.py
from AppWeb.forms import ProveedorFormulario #importe el formulario
from django.http import HttpResponse

# Create your views here.

def inicio (request):
    return render(request, "AppWeb/inicio.html")

def prov (request):
    return render(request, "AppWeb/prov.html")

def cliente (request):
    return render(request, "AppWeb/clientes.html")

def item (request):
    return render(request, "AppWeb/items.html")

def prueba (request):
    return render(request, "AppWeb/form_prov.html")



#para agregar datos
def agregar_prov(request):
    nuevo_formulario=ProveedorFormulario()
    if request.method == "POST":  #si el formulario tiene el metodo post q avance

       nuevo_formulario=ProveedorFormulario(request.POST)

       if nuevo_formulario.is_valid():
           
           info=nuevo_formulario.cleaned_data
           
           prov_nuevo=Proveedor(nombre=info["nombre"],condicion=info["condicion"]) #para los value tomo los nombre de la clase form

           prov_nuevo.save()

           return render(request, "AppWeb/inicio.html") #para q me lleve a la pag de inicio luego de guadar
       

    return render(request, "AppWeb/form_prov.html", {"mi_formu":nuevo_formulario})



def buscar_prov(request):
        
        return render(request, "AppWeb/buscar_prov.html")


def resul_prov(request):

    if request.method=='GET':

        prov_pedido=request.GET['nombr']
        resul_prov=Proveedor.objects.filter(nombre__icontains=prov_pedido)

        return render(request, "AppWeb/buscar_prov.html", {"provs":resul_prov})
    else:
        return render(request, "AppWeb/buscar_prov.html")




