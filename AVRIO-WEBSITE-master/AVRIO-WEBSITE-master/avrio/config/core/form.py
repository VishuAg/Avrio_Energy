from django import forms
from core.models import form
from django.core import validators
class NewUser(forms.ModelForm):
    class Meta:
        model = form
        fields='__all__'
