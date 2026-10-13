
# forms: trae las herramientas de Django para construir formularios
from django import forms

# Servicio: el modelo de la Unidad 2
from .models import Servicio

# Formulario generado a partir del modelo Servicio
class ServicioForm(forms.ModelForm):
    class Meta:
        # Modelo del que se generan los campos
        model = Servicio

        # Campos que aparecerán en el formulario
        # propietario se asignará automáticamente en la vista
        fields = ['titulo', 'descripcion', 'precio', 'categoria']
