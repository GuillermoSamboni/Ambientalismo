from .serializer import *
from home.models import *
from rest_framework import viewsets

class lugar_viewset (viewsets.ModelViewSet):
    queryset= Lugar.objects.all()
    serializer_class=lugar_serializer

class animal_viewset (viewsets.ModelViewSet):
    queryset= Animal.objects.all()
    serializer_class=animal_serializer

class noticia_viewset(viewsets.ModelViewSet):
    queryset= Noticia.objects.all()
    serializer_class=noticia_serializer