from django.urls import path
from .views import *

urlpatterns=[
    path('',vista_about, name='vista_about'),
    path('contacto/',vista_contacto, name='vista_contacto'),
    
    #urls de lugares
    path('lugares/',vista_lista_lugares, name='vista_lista_lugares'),
    path('agregar_lugar/',vista_agregar_lugar, name='vista_agregar_lugar'),

    path('ver_lugar/<int:id_lugar>', vista_ver_lugar, name='vista_ver_lugar'),
    path('eliminar_lugar/<int:id_lugar>', vista_eliminar_lugar, name='vista_eliminar_lugar'),
    path('editar_lugar/<int:id_lugar>', vista_editar_lugar, name='vista_editar_lugar'),

    #urls de animales
    path('animales/', vista_lista_animales, name ='vista_lista_animales'),
    path('agregar_animal/', vista_agregar_animal, name='vista_agregar_animal'),

    path('ver_animal/<int:id_animal>', vista_ver_animal, name='vista_ver_animal'),
    path('eliminar_animal/<int:id_animal>', vista_eliminar_animal, name='vista_eliminar_animal'),
    path('editar_animal/<int:id_animal>', vista_editar_animal, name='vista_editar_animal'),

    
    #urls de noticias
    path('noticias/', vista_lista_noticias, name='vista_lista_noticias'),
    path('agregar_noticia/', vista_agregar_noticia, name='vista_agregar_noticia'),

    path('ver_noticia/<int:id_noticia>', vista_ver_noticia, name='vista_ver_noticia'),
    path('eliminar_noticia/<int:id_noticia>', vista_eliminar_noticia, name='vista_eliminar_noticia'),
    path('editar_noticia/<int:id_noticia>', vista_editar_noticia, name='vista_editar_noticia'),

    path('login/', vista_login, name="vista_login"),
    path('logout/', vista_logout, name="vista_logout"),

    ]