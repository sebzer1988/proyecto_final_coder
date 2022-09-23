from re import template
from django.urls import path
from AppCuentas.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("paginaCuentas/", paginaCuentas, name="paginaCuentas"),
    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(template_name="AppCuentas/logout.html"), name="logout"),
    path("editarPerfil/", editarPerfil, name="editarPerfil"),
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),
    path("perfil/<pk>", userDetalle.as_view(), name="getPerfil"),


]