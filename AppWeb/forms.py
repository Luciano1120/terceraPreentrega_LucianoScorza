from django import forms  #se crea este archivo

#copiar el modelo y cambiar por form. se puede usar changeallocurrences

class ProveedorFormulario(forms.Form):

    id=forms.IntegerField
    nombre=forms.CharField(max_length=30)
    condicion=forms.CharField(max_length=30)