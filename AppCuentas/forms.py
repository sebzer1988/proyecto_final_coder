from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}


class UserEditForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)
    web= forms.CharField(label="Sitio web")

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
        help_texts = {k: "" for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")