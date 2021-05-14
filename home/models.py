from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length = 100)
    def __str__ (self):
        return self.nombre

class Noticia(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion= models.TextField(max_length= 500)
    def __str__ (self):
        return self.nombre

class Animal(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion= models.TextField(max_length= 500)
    def __str__ (self):
        return self.nombre

class Lugar(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion= models.TextField(max_length= 500)
    localizacion= models.CharField(max_length=100)
    def __str__ (self):
        return self.nombre

