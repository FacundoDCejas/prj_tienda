from django.db.models.base import Model
from django.forms import ModelForm, widgets
from .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type= 'date'

class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'num_doc': forms.TextInput(attrs={'type': 'number', 'class': 'form-control input'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize',
                                               'placeholder': 'Apellido'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize',
                                               'placeholder': 'Nombre'}),
            'fecha_nac': DateInput(format='%Y-%m-%d',attrs={'class':'form-control input-sm'}),
            'localidad':forms.Select(attrs={'class':'form-control input'})
        }


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'


class MovimientoForm(ModelForm):
    class Meta:
        model = Movimiento
        fields = '__all__'


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
