from django.contrib import admin
from AppWeb.models import *  #agrego esta linea para traer todos lo modelos al admin de django

# Register your models here.


#para agregar los modelos al panel de administracion de django
admin.site.register(Item)
admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(avatar)

