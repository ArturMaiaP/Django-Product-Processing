from django import forms
from .models import Rule
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields =[
            'cor',
            'tipo',
            'codigo_gtin'
        ]

class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule

        fields =[
            'field',
            'value'
        ]

