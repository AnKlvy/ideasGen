from django import forms
from .models import *


class ContGener(forms.Form):
    keywords = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control'}));
