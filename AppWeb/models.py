from django.db import models
from django.contrib.auth.models import User #la tenia importada de archivo forms.py y ahora tambien la necesito acá por lo q la copio

# Create your models here.

#creo 3 modelos-- desde esta linea lo hago yo
#los modelos se vinculan a la BD
class Item(models.Model):

    id=models.IntegerField  #el campo de nombre id lo identifica como PK, por no debe ponerse () luego de intergerfield, si fuera otro campo si se pondría()- Ver el error q sale: AppWeb.Item: (models.E004) 'id' can only be used as a field name if the field also sets 'primary_key=True'.
    #No hace falta pasar el id como parametro en el Insert ya q al ser PK entra solo
    nombre=models.CharField(max_length=30)
    categoria=models.CharField(max_length=15)
    #foto=models.ImageField (ver de agregar este campo cuando vea el resumen de carga de foto)
    

class Cliente(models.Model):

    id=models.IntegerField
    nombre=models.CharField(max_length=30)
    CUIT=models.CharField(max_length =10, default='000')  #este campo lo agregué después y necesita un valor por default una vez creado el modelo
    #si se agrega un campo nuevo voy a tener q hacer siempre las makemigrations y migrate, pero darle un valor por default

class Proveedor(models.Model):

    #con el metodo str permite q en el panel de django este modelo se vea mas legible
    def __str__(self):
        return f"Nombre: {self.nombre} ----- Cuit: {self.CUIT} ---- {self.condicion} "

    id=models.IntegerField
    nombre=models.CharField(max_length=30)
    CUIT=models.CharField(max_length =10, default='000')
    condicion=models.CharField(max_length=30)

#es necesario q cada modelo q se cree agregarlo en admin.py
class avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #lo vinculo con la Clase User, y on delete Cascade es para q si se elimina el usuario se elimine el avatar
    imagen = models.ImageField(upload_to="avatares", null=True , blank=True) # ya q no todos los usuarios va a tener Avatares por eso null y blank = True

    def __str__(self):
        return f"{self.usuario} --- {self.imagen}"
                    



