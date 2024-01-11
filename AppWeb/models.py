from django.db import models

# Create your models here.

#creo 3 modelos-- desde esta linea lo hago yo
class Item(models.Model):

    id=models.IntegerField
    nombre=models.CharField(max_length=30)
    categoria=models.CharField(max_length=15)

class Cliente(models.Model):

    id=models.IntegerField
    nombre=models.CharField(max_length=30)
    CUIT=models.IntegerField()  #no me lo está creando

class Proveedor(models.Model):

    id=models.IntegerField
    nombre=models.CharField(max_length=30)
    condicion=models.CharField(max_length=30)