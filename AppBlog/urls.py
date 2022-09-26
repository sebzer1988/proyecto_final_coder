from re import template
from django.urls import path
from AppBlog.views import *

urlpatterns = [
    path("inicioblog/", inicio_blog, name="inicioblog"),
    path("Articulo/list/", ArticuloList.as_view(), name="articulo_listar"),
    path("Articulo/<pk>", ArticuloDetalle.as_view(), name="articulo_detalle"),
    path("Articulo/nuevo/", ArticuloCreacion.as_view(), name="articulo_crear"),
    path("Articulo/editar/<pk>", ArticuloUpdate.as_view(), name="articulo_editar"),
    path("Articulo/borrar/<pk>", ArticuloDelete.as_view(), name="articulo_borrar"),
    
    

]