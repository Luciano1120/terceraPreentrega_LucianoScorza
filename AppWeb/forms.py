from django import forms  #se crea este archivo
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

#copiar el modelo y cambiar por form. se puede usar changeallocurrences

class ProveedorFormulario(forms.Form):

    

    id=forms.IntegerField
    nombre=forms.CharField(max_length=30)
    CUIT=forms.CharField(max_length =10)
    condicion=forms.CharField(max_length=30)


class UsuarioRegistro(UserCreationForm):
#para agregar mas campos al registro
    email = forms.EmailField()
    password1 = forms.CharField(label= "Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir Contraseña", widget= forms.PasswordInput)

    class Meta:

        model = User
        fields=["username", "email", "first_name","last_name","password1","password2" ] #así los requiere django

