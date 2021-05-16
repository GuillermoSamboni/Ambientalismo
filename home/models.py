from django.db import models

# Create your models here.

class Animal(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion= models.TextField(max_length= 500)
    foto= models.ImageField(upload_to= 'animales', null=True, blank= True)
    video= models.FileField(upload_to="video_animal", null=True, blank=True)

    def __str__ (self):
        return self.nombre

class Noticia(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion= models.TextField(max_length= 500)
    foto= models.ImageField(upload_to= 'noticias', null=True, blank= True)
    video= models.FileField(upload_to="video_noticas", null=True, blank=True)
    #animal= models.ForeignKey(Animal, models.PROTECT)

    def __str__ (self):
        return self.nombre

class Lugar(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion= models.TextField(max_length= 500)
    localizacion= models.CharField(max_length=100)
    foto= models.ImageField(upload_to= 'lugares', null=True, blank= True)
    video= models.FileField(upload_to="video_lugares", null=True, blank=True)

    #animal=models.ForeignKey(Animal, models.PROTECT)

    def __str__ (self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length = 100)

    def __str__ (self):
        return self.nombre