from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from AppBlog.models import *

def inicio_blog(request):
    return render (request, "Blog/blog.html")

class ArticuloList(LoginRequiredMixin, ListView):
    model=articulo
    template_name= "Blog/leer_articulo.html"

class ArticuloDetalle(DetailView):
    model=articulo
    template_name= "Blog/articulo_detalle.html"

class ArticuloCreacion(CreateView):
    model = articulo
    success_url = reverse_lazy("articulo_listar")
    fields=["titulo", "imagen", "autor", "contenido", "slug", "creacion"]

class ArticuloUpdate(UpdateView):
    model = articulo
    success_url = reverse_lazy("articulo_listar")
    fields=["titulo", "imagen", "autor", "contenido", "slug", "creacion"]

class ArticuloDelete(DeleteView):
    model = articulo
    success_url = reverse_lazy("articulo_listar")
