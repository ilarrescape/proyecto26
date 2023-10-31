from django import forms
from .models import Pais, Provincia, Ciudad

class CiudadForm(ModelForm):
    class Meta:
        model = Ciudad
        fields = "__all__"