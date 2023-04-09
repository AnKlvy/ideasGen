from django import forms
from .models import *


class ContGener(forms.Form):
    # slug = forms.SlugField(max_length=255)
    keywords = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control'}));

