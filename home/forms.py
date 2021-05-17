from django import forms
from django.contrib.auth.models import User
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

class register_user_form(forms.Form):
    usuario= forms.CharField(widget=forms.TextInput())
    correo= forms.EmailField(widget=forms.TextInput())
    contraseña=forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False))
    confirmar=forms.CharField(label='confirmar password', widget=forms.PasswordInput(render_value=False))

    def clean_username(self):
        usuario=self.cleaned_data['usuario']
        try:
            u=User.objects.get(username=usuario)
        except User.DoesNotExist:
            return usuario
        raise forms.validationError('Nombre de usuario ya registrado')
    
    def clean_correo(self):
        correo=self.cleaned_data['correo']
        try:
            correo=User.objects.get(email=correo)
        except User.DoesNotExist:
            return correo
        raise forms.validationError('Este correo ya esta registrado')
    
    def clean_passwod(self):
        password_1=self.cleaned_data['password_1']
        password_2=self.cleaned_data['password_2']

        if password_1==password_2:
            pass
        else:
            raise forms.validationError('las contraseñas no coinciden')


