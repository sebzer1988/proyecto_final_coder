from audioop import reverse
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader

def inicio(request):
    return render (request, "inicio.html")

def about(request):
    return render (request, "about.html")

def padre(request):
    return render (request, "padre.html")