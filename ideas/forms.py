from django import forms
from .models import *


class ContGener(forms.Form):
    keywords = forms.CharField(max_length=1000, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Type keywords'}))


class OwnIdeaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Ideas
        fields = ['idea', 'user']
        widgets = {
            'idea': forms.TextInput(attrs={'class': 'form-control'})
        }
