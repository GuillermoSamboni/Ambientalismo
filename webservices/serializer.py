from rest_framework import serializers
from home.models import *
#from .serializer import *

# Create your views here.

class lugar_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Lugar
        fields=('url','nombre','descripcion','localizacion')
class animal_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Animal
        fields=('url','nombre','descripcion')

class noticia_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Noticia
        fields=('url','nombre','descripcion')
