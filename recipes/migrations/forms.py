from django import forms
from django.contrib.auth.models import User
from . import models


class ClientUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['prenom', 'nom', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']


# addresse de livraison
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile = forms.IntegerField()
    Address = forms.CharField(max_length=500)


class AvisForm(forms.ModelForm):
    class Meta:
        model = models.avis
        fields = ['nom', 'avis']