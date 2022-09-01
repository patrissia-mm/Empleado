from socket import fromshare
from tkinter import Widget
from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for MODELNAME."""
    class Meta:
        """Meta definition for MODELNAMEform."""
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el título aquí'
                }
            ),
            'subtitulo': forms.TextInput(attrs={'placeholder': 'Ingrese subtítulo aquí'}),
            'cantidad': forms.NumberInput(attrs={'placeholder': 'Ingrese una cantidad > o = a 10'})
        }
    
    def clean_cantidad(self):
        cant = self.cleaned_data['cantidad']
        if cant < 10:
            raise forms.ValidationError('Introduzca un número mayor o igual a 10')
        return cant
