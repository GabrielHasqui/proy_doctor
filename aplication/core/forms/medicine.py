from django.forms import ModelForm, ValidationError
from django import forms
from aplication.core.models import Medicamento

class MedicineForm(ModelForm):
    class Meta:
        model = Medicamento 
        fields = ['nombre', 'tipo', 'marca_medicamento', 'descripcion', 
              'concentracion', 'cantidad', 'precio', 'comercial', 'activo', 'imagen']
        
        error_messages = {
            'nombre': {
            'required': "El campo nombre es requerido"
            },
            'tipo': {
            'required': "El campo tipo es requerido"
            },
            'marca_medicamento': {
            'required': "El campo marca medicamento es requerido"
            },
            'descripcion': {
            'required': "El campo descripcion es requerido"
            },
            'concentracion': {
            'required': "El campo concentracion es requerido"
            },
            'cantidad': {
            'required': "El campo cantidad es requerido"
            },
            'precio': {
            'required': "El campo precio es requerido"
            },
            'comercial': {
            'required': "El campo comercial es requerido"
            },
            'imagen': {
            'required': "El campo imagen es requerido"
            }
        }
        
        widgets = {
            'nombre': forms.TextInput(
            attrs={
                "placeholder": "Ingrese nombre",
                "id": "id_nombre",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }
            ),
            'tipo': forms.Select(
            attrs={
                "placeholder": "Ingrese tipo",
                "id": "id_tipo",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }
            ),
            'marca_medicamento': forms.Select(
            attrs={
                "placeholder": "Ingrese marca medicamento",
                "id": "id_marca_medicamento",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }
            ),
            'descripcion': forms.TextInput(
            attrs={
                "placeholder": "Ingrese descripcion",
                "id": "id_descripcion",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }
            ),
            'concentracion': forms.TextInput(
            attrs={
                "placeholder": "Ingrese concentracion",
                "id": "id_concentracion",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }
            ),
            'cantidad': forms.TextInput(
            attrs={
                "placeholder": "Ingrese cantidad",
                "id": "id_cantidad",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }
            ),
            'precio': forms.TextInput(
            attrs={
                "placeholder": "Ingrese precio",
                "id": "id_precio",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }
            ),
            'comercial': forms.TextInput(
            attrs={
                "placeholder": "Ingrese comercial",
                "id": "id_comercial",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }
            ),
            'activo': forms.CheckboxInput(
            attrs={
                "id": "id_activo",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }
            ),
            'imagen': forms.FileInput(
            attrs={
                "placeholder": "Ingrese imagen",
                "id": "id_imagen",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }
            ),
        }