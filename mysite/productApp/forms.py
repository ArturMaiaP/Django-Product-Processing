from django import forms
from .models import Product

class ProducForm(forms.Form):
    cor = forms.CharField(label='Cor', max_length=200)
    tipo = forms.CharField(label='Tipo', max_length=200)
    codigo_gtin = forms.CharField(label='Codigo gtin', max_length=200)

