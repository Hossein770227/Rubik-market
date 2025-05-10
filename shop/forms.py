from django import forms

from .models import CommentPhone


class CommentPhoneForm(forms.ModelForm):
    class Meta:
        model = CommentPhone
        fields = ['email','text','score']
