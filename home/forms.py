from django import forms
from .models import *

class contacto_form(forms.Form):
    correo = forms.EmailField(widget = forms.TextInput())
    titulo = forms.CharField(widget = forms.TextInput())
    texto = forms.CharField(widget = forms.Textarea())

class agregar_lugar_form(forms.ModelForm):
    class Meta:
        model= Lugar
        fields= '__all__'

class agregar_animal_form(forms.ModelForm):
    class Meta:
        model= Animal
        fields='__all__'

class agregar_noticia_form(forms.ModelForm):
    class Meta:
        model= Noticia
        fields='__all__'

class iniciar_sesion_form(forms.Form):
    usuario=forms.CharField(widget=forms.TextInput())
    clave=forms.CharField(widget=forms.PasswordInput(render_value=False))
