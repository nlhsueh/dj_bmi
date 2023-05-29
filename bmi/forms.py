from django import forms
from .models import People
from django.core.exceptions import ValidationError

class PeopleModelForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['pname', 'h', 'w'] 

        widgets = {
            'pname': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}), 
            'h': forms.NumberInput(attrs={'class': 'form-control'}), 
            'w': forms.NumberInput(attrs={'class': 'form-control'}),
        }
