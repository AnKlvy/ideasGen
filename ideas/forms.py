from django import forms
from .models import *
from django.contrib.auth.models import User




class ContGener(forms.Form):
    keywords = forms.CharField(max_length=1000, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Type keywords'}))


class OwnIdeaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # self.fields['user'].queryset = User.objects.filter(id=self.request.user.id)

    class Meta:
        model = Ideas
        fields = ['idea']
        widgets = {
            'idea': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Share your idea'}),
            # 'user': forms.HiddenInput()
        }

# class OwnIdeaForm(forms.ModelForm):
#     idea = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Share your idea'}))
#     user = forms.ModelChoiceField(queryset=User.objects.none())
#
#     def __init__(self, *args, **kwargs):
#         request = kwargs.pop('request', None)
#         super(OwnIdeaForm, self).__init__(*args, **kwargs)
#         if request:
#             self.request = request
#             self.fields['user'].queryset = User.objects.filter(id=self.request.user.id)
#
#     class Meta:
#         model = Ideas
#         fields = ('idea', 'user',)
