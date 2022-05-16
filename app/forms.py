from dataclasses import field
from operator import imod
from django import forms
from django.forms import ModelForm
from .models import *

#Creamos un template para el formulario
class ProductoForm(ModelForm):
    
    nombre = forms.CharField(min_length=10,max_length=20)
    precio = forms.IntegerField(min_value=400)

    class Meta:
        model= Producto
        fields=['codigo','nombre','raza','stock','descripcion','precio','tipo','imagen']

        #widgets = {
        #    'fecha_ingreso' : forms.SelectDateWidget(years=range(2020,2023))
        #}

class UsuarioForm(ModelForm):
    
    class Meta:
        model= Usuario
        fields=['rut','nombre','apellido','contraseña','comuna','direccion']

        #widgets = {
        #    'fecha_ingreso' : forms.SelectDateWidget(years=range(2020,2023))
        #}