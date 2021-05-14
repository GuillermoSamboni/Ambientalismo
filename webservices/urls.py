from django.urls import path, include
from rest_framework import routers
from home.models import *
from webservices.views import *

router = routers.DefaultRouter()
router.register(r'lugares', lugar_viewset)
router.register(r'animales', animal_viewset)
router.register(r'noticias', noticia_viewset)

urlpatterns=[
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]