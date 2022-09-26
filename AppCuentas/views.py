from audioop import reverse
from http.client import HTTPResponse
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import Context, Template, loader
from AppCuentas.forms import *

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def paginaCuentas(request):
    return render (request, "paginaCuentas.html")

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCuentas/login.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppCuentas/login.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "AppCuentas/login.html", {"formulario":form})

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render(request, "inicio.html", {"mensaje": f"Usuario {username} creado correctamente"})
        else:
            return render (request, "AppCuentas/register.html", {"formulario":form, "mensaje":"FORMULARIO INVALIDO"})
    else:
        form=UserRegisterForm()
        return render (request, "AppCuentas/register.html", {"formulario":form})
        
login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.username=info["username"]
            usuario.email=info["email"]
            usuario.password=info["password1"]
            usuario.password=info["password2"]
            usuario.save()
            return render(request, "AppCuentas/getPerfil.html", {"mensaje":"Perfil editado correctamente"})
        else:
            return render (request, "AppCuentas/editarPerfil.html", {"formulario":form, "usuario":usuario, "mensaje":"FORMULARIO INVALIDO"})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "AppCuentas/editarPerfil.html", {"formulario":form, "usuario":usuario})


@login_required
def agregarAvatar(request):
    if request.method=="POST":
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()

            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data["imagen"])
            avatar.save()
            return render(request, "AppCuentas/getPerfil.html", {"usuario":request.user, "mensaje":"Avatar cambiado"})
        else:
            return render(request, "AppCuentas/agregarAvatar.html", {"formulario":formulario, "mensaje":"Formulario invalido"})
    else:
        formulario=AvatarForm()
        return render(request, "AppCuentas/agregarAvatar.html", {"formulario":formulario, "usuario":request.user})


def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/avatar1.png"
    return imagen

def getPerfil(request):
    return render(request, "AppCuentas/getPerfil.html", {"mensaje":"Gracias","avatar":obtenerAvatar(request)})