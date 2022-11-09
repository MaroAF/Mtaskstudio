from distutils.command.upload import upload
from enum import unique
from tkinter import image_names
from django.db import models
from ckeditor.fields import RichTextField
from pkg_resources import require

# Create your models here.

#Main Page
class Header(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/main',verbose_name='Logo')
    number = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("Cabecera")
        verbose_name_plural = ("Cabecera")

#other
class Schedule(models.Model):
    title = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100, unique=True,verbose_name='Link Automatico (NO MODIFICAR)')
    image_v = models.ImageField(upload_to='images/Sessions',verbose_name='Imagen vertical(Portada del Set)')
    image_h = models.ImageField(null=True,blank=True,upload_to='images/Sessions',verbose_name='Imagen Banner(Si se requiere)')
    active = models.BooleanField(default=False)
    image_v1 = models.ImageField(upload_to='images/Sessions',verbose_name='Imagen vertical Foto demostrativa 1')
    image_v2 = models.ImageField(upload_to='images/Sessions',verbose_name='Imagen vertical Foto demostrativa 2')
    image_v3 = models.ImageField(upload_to='images/Sessions',verbose_name='Imagen vertical Foto demostrativa 3')    
    content = RichTextField(null=True,blank=True,verbose_name='Contenido')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("Set")
        verbose_name_plural = ("Sets")
    
class Placeholder(models.Model):
    title = models.CharField(max_length=100,unique=True)
    image = models.ImageField(upload_to='images/general',verbose_name='Imagen que se descargara')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("Imagen negra")
        verbose_name_plural = ("Imagenes en negro")
