from django import forms
# from forms import Mo
from .models import tempModel

class tempForm(forms.ModelForm):
    class Meta:
        model = tempModel
        fields="__all__"
        



