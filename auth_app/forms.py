
from django import forms
from .models import Register

class form_class(forms.ModelForm):
    class Meta:
        model= Register
        fields='__all__'