from django import forms
from .models import Produit

from django.contrib.auth.forms import AuthenticationForm

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'
# In forms.py
from django import forms

class LoginForm(AuthenticationForm):
    # Si tu veux personnaliser les champs, tu peux les redéfinir ici
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

