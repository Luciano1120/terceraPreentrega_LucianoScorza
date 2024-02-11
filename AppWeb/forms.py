#debemos crear este archivo con el nombre forms.py

from django import forms  
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from  AppWeb.models import avatar

#copiar del modelo y cambiar por form. se puede usar "changeallocurrences" q sería como un reemplazar
#es una clase muy similar a la de modelo q me permite la carga de datos al modelo a traves de un formulario q paso al HTML para el usuario

#similar a crear un modelo pero creamos acá la clase formulario
class ProveedorFormulario(forms.Form):

    id=forms.IntegerField
    nombre=forms.CharField(max_length=30)
    CUIT=forms.CharField(max_length =10)
    condicion=forms.CharField(max_length=30)


class UsuarioRegistro(UserCreationForm):
#para agregar mas campos al registro, o editar los labels
    username= forms.CharField(label= "Ingrese su Nombre de Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label= "Contraseña", widget= forms.PasswordInput, help_text= "al menos 8 Caracteres") #el help text es para q salga auna ayuda memoria
    password2 = forms.CharField(label= "Repetir Contraseña", widget= forms.PasswordInput)

    class Meta:

        model = User
        fields=["username", "email", "first_name","last_name","password1","password2" ] #así los requiere django

class formularioEditarUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= "Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir Contraseña", widget= forms.PasswordInput)

    class Meta:

        model = User
        fields=["email", "first_name","last_name","password1","password2" ] #no requiere editar el username, ya q no es lo q se acostumbra


class AvatarFormulario(forms.ModelForm):  #en vez de .Form uso .ModelForm

    class Meta:

        model = avatar  #es el modelo importado
        fields=[ "imagen"]

    


    
