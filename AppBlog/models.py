from datetime import datetime
from operator import mod
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



class articulo(models.Model): #Aca se ingresa los articulos

    
    titulo = models.CharField(max_length=100) 
    imagen = models.ImageField(null=True, blank=True, upload_to="")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    slug = models.SlugField(editable=False)
    creacion = models.DateTimeField(default=datetime.utcnow)

    def __unicode__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(articulo, self).save(*args, **kwargs)

