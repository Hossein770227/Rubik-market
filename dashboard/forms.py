from django import forms

from .models import Address 

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['province','city','full_address','postal_code',]