from re import template
from django.urls import path
from AppBlog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("blog/", blog, name="blog"),

]