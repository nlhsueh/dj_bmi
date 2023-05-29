from django import forms
from .models import People
from django.core.exceptions import ValidationError

class PeopleModelForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['pname', 'h', 'w'] 
