from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def vista_about(request):
    noticias= Noticia.objects.filter() #SELECT FROM *
    return render(request, 'about.html', locals())
#vista contacto
def vista_contacto(request):
    info_enviado= False
    email = ""
    title = ""
    text = ""
    if request.method == "POST":
        formulario= contacto_form(request.POST)
        if formulario.is_valid():
            info_enviado = True
            email= formulario.cleaned_data["correo"]
            title= formulario.cleaned_data["titulo"]
            text= formulario.cleaned_data["texto"]
    else:
        formulario= contacto_form()

    return render(request, 'contacto.html', locals())

#vista de todos los lugares
def vista_lista_lugares(request):
    lugares= Lugar.objects.filter()
    return render(request,'lugares.html', locals())
#vista agregar un nuevo lugar
def vista_agregar_lugar(request):
    if request.method =='POST':
        formulario=agregar_lugar_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/lugares/')
    else:    
        formulario = agregar_lugar_form()
    return render(request,'agregarlugar.html', locals())
#vista de un solo lugar por su id
def vista_ver_lugar(request, id_lugar):
    detalle= Lugar.objects.get(id=id_lugar)#SELECT FROM * NOMBRETABLA WHERE ID= ID_lugar
    return render(request, 'verLugar.html', locals())
#vista de eliminar un lugar  
def vista_eliminar_lugar(request, id_lugar):
    objeto= Lugar.objects.get(id=id_lugar)
    objeto.delete()
    return redirect('/lugares/')
#vista de editar un lugar
def vista_editar_lugar(request, id_lugar):
    objeto= Lugar.objects.get(id=id_lugar)
    if request.method=='POST':
        formulario=agregar_lugar_form(request.POST, instance= objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/lugares/')
    else:        
        formulario= agregar_lugar_form(instance= objeto)

    return render(request, 'agregarlugar.html', locals())


#vista de todos los animales
def vista_lista_animales(request):
    animales = Animal.objects.filter() #SELECT FROM *
    return render(request, 'animales.html', locals())
#vista de agregar un nuevo animal
def vista_agregar_animal(request):
    if request.method=='POST':
        formulario=agregar_animal_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/animales/')
    else:
        formulario=agregar_animal_form()
    return render(request, 'agregarAnimal.html', locals())
#vista de una solo animal por su id
def vista_ver_animal (request, id_animal):
    detalle= Animal.objects.get(id=id_animal)#SELECT FROM * NOMBRETABLA WHERE ID= ID_animal
    return render(request, 'verAnimal.html', locals())
#vista de eliminar un solo animal  
def vista_eliminar_animal (request, id_animal):
    objeto= Animal.objects.get(id=id_animal)
    objeto.delete()
    return redirect('/animales/')
#vista de editar un solo animal
def vista_editar_animal (request, id_animal):
    objeto= Animal.objects.get(id=id_animal)
    if request.method=='POST':
        formulario=agregar_animal_form(request.POST, instance= objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/animales/')
    else:        
        formulario= agregar_noticia_form(instance= objeto)

    return render(request, 'agregarAnimal.html', locals())


#vista de todas las noticas
def vista_lista_noticias(request):
    noticias= Noticia.objects.filter() #SELECT FROM *
    return render(request,'noticias.html', locals())
#vista de agregar un nuevo NOTICIA
def vista_agregar_noticia(request):
    if request.method=='POST':
        formulario=agregar_noticia_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/noticias/')
    else:
        formulario=agregar_noticia_form()
    return render(request, 'agregarNoticia.html', locals())
#vista de una solo noticia por su id
def vista_ver_noticia(request, id_noticia):
    detalle= Noticia.objects.get(id=id_noticia)#SELECT FROM * NOMBRETABLA WHERE ID= ID_noticia
    return render(request, 'verNoticia.html', locals())
#vista de eliminar una noticia  
def vista_eliminar_noticia(request, id_noticia):
    objeto= Noticia.objects.get(id=id_noticia)
    objeto.delete()
    return redirect('/noticias/')
#vista de editar una noticia
def vista_editar_noticia(request, id_noticia):
    objeto= Noticia.objects.get(id=id_noticia)
    if request.method=='POST':
        formulario=agregar_noticia_form (request.POST, instance= objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/noticias/')
    else:        
        formulario= agregar_noticia_form(instance= objeto)

    return render(request, 'agregarNoticia.html', locals())
