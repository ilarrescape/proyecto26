
from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('documento', 'nombre', 'apellido', 'telefono')
