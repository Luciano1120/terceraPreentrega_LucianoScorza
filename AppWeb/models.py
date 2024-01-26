from django.db import models

# Create your models here.

#creo 3 modelos-- desde esta linea lo hago yo
class Item(models.Model):

    id=models.IntegerField
    nombre=models.CharField(max_length=30)
    categoria=models.CharField(max_length=15)
    #foto=models.ImageField (ver de agregar este campo cuando vea el resumen de carga de foto)
    

class Cliente(models.Model):

    id=models.IntegerField
    nombre=models.CharField(max_length=30)
    CUIT=models.CharField(max_length =10, default='000')  #este campo lo agregué después y necesita un valor por default una vez creado el modelo

class Proveedor(models.Model):

    #con el metodo str permite q en el panel de django este modelo se vea mas legible
    def __str__(self):
        return f"Nombre: {self.nombre} ----- Cuit: {self.CUIT} ---- {self.condicion} "

    id=models.IntegerField
    nombre=models.CharField(max_length=30)
    CUIT=models.CharField(max_length =10, default='000')
    condicion=models.CharField(max_length=30)
