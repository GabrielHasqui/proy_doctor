import datetime
from django.forms import ModelForm, ValidationError
from django import forms
from aplication.attention.models import ExamenSolicitado

class RequestedExamForm(ModelForm):
    class Meta:
        model = ExamenSolicitado
        fields = ['nombre_examen', 'paciente', 'resultado', 'comentario', 'estado']
        
        error_messages = {
            'nombre_examen': {
                'required': "El nombre del examen es requerido"
            },
            'paciente': {
                'required': "El campo paciente es requerido"
            },
            'estado': {
                'required': "El estado del examen es requerido"
            }
        }
        
        widgets = {
            'nombre_examen': forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombre del examen",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'paciente': forms.Select(
                attrs={
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'resultado': forms.FileInput(
                attrs={
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'comentario': forms.Textarea(
                attrs={
                    "placeholder": "Ingrese comentarios",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'estado': forms.Select(
                attrs={
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            )
        }
        def clean_nombre_examen(self):
            nombre_examen = self.cleaned_data.get('nombre_examen')
            if not nombre_examen:
                raise ValidationError("El nombre del examen es requerido")
            return nombre_examen

        def clean_paciente(self):
            paciente = self.cleaned_data.get('paciente')
            if not paciente:
                raise ValidationError("El campo paciente es requerido")
            return paciente

        def clean_estado(self):
            estado = self.cleaned_data.get('estado')
            if not estado:
                raise ValidationError("El estado del examen es requerido")
            return estado